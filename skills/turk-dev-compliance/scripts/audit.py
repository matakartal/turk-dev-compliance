#!/usr/bin/env python3
"""turk-dev-compliance denetim tarayıcısı (yalnızca okur, dosya değiştirmez).

Kullanım: python3 audit.py <proje_dizini> [--json]

Bulur:
  - uzak font/CDN/script/embed URL'leri (olası yurt dışı aktarım, IP sızıntısı)
  - bilinen izleyici / analitik / reklam / hata izleme SDK'ları
  - rıza öncesi yüklenebilecek analitik etiketleri
  - ön işaretli onay kutuları (checked / defaultChecked / isOn: true)
  - log satırlarında olası kişisel veri
  - LLM API çağrıları (kişisel veri gönderiliyorsa yurt dışı aktarım)
Çıktı bulgu listesidir; hüküm değildir. Her bulgu manuel doğrulama ister.
"""
import json
import os
import re
import sys

SKIP_DIRS = {".git", "node_modules", "dist", "build", ".next", ".venv", "venv",
             "Pods", "DerivedData", ".gradle", "vendor", "__pycache__"}
EXTS = {".html", ".htm", ".css", ".scss", ".js", ".jsx", ".ts", ".tsx", ".vue",
        ".svelte", ".php", ".py", ".rb", ".go", ".java", ".kt", ".swift",
        ".json", ".gradle", ".plist", ".xml", ".yml", ".yaml", ".toml", ".md",
        ".erb", ".twig", ".blade.php"}
MAX_BYTES = 1_500_000

REMOTE_HOSTS = {
    "fonts.googleapis.com": ("uzak-font", "Google Fonts: ziyaretçi IP'si Google'a gider. Self-host edin."),
    "fonts.gstatic.com": ("uzak-font", "Google Fonts dosyası: self-host edin."),
    "use.typekit.net": ("uzak-font", "Adobe Fonts: üçüncü taraf istek."),
    "use.fontawesome.com": ("uzak-font", "Font Awesome CDN: self-host edin."),
    "cdnjs.cloudflare.com": ("uzak-script", "Üçüncü taraf CDN: paketi kendi sunucunuzdan servis edin."),
    "cdn.jsdelivr.net": ("uzak-script", "Üçüncü taraf CDN: paketi kendi sunucunuzdan servis edin."),
    "unpkg.com": ("uzak-script", "Üçüncü taraf CDN: paketi kendi sunucunuzdan servis edin."),
    "code.jquery.com": ("uzak-script", "Üçüncü taraf CDN."),
    "maps.googleapis.com": ("embed", "Google Maps: yurt dışı aktarım + çerez; rıza/alternatif düşünün."),
    "www.google.com/maps": ("embed", "Google Maps embed."),
    "www.google.com/recaptcha": ("embed", "reCAPTCHA: üçüncü taraf veri toplar; aydınlatmada belirtin."),
    "www.gstatic.com/recaptcha": ("embed", "reCAPTCHA."),
    "www.youtube.com/embed": ("embed", "YouTube embed: youtube-nocookie + rıza sonrası yükleme düşünün."),
    "player.vimeo.com": ("embed", "Vimeo embed."),
    "gravatar.com": ("embed", "Gravatar: e-posta hash'i dışarı gider."),
    "platform.twitter.com": ("embed", "Sosyal medya widget'ı."),
    "connect.facebook.net": ("izleyici", "Meta SDK/Pixel: rıza öncesi yüklenmemeli."),
}

TRACKERS = {
    r"googletagmanager\.com|gtag\(|google-analytics\.com|GoogleAnalytics|firebase[_-]?analytics|FIRAnalytics":
        ("izleyici", "Google Analytics/GTM/Firebase Analytics: rıza + yurt dışı aktarım."),
    r"fbq\(|facebook-pixel|FBSDKCoreKit|facebook-android-sdk":
        ("izleyici", "Meta Pixel/SDK: rıza + yurt dışı aktarım."),
    r"hotjar|clarity\.ms|fullstory|mixpanel|amplitude|segment\.com|posthog|heap\.io":
        ("izleyici", "Davranış analitiği/oturum kaydı: rıza + yurt dışı aktarım."),
    r"sentry\.io|@sentry/|Sentry\.init|bugsnag|crashlytics|Crashlytics":
        ("hata-izleme", "Hata izleme: kullanıcı verisi (IP, e-posta) gönderiyor olabilir; maskeleyin."),
    r"intercom|crisp\.chat|zendesk|tawk\.to|hubspot":
        ("destek-widget", "Canlı destek/CRM widget'ı: veri işleyen sözleşmesi + yurt dışı aktarım."),
    r"adjust\.com|appsflyer|branch\.io|AppsFlyer|Adjust\.|singular\.net":
        ("izleyici", "Mobil atıf/izleme SDK'sı."),
    r"admob|GADMobileAds|GoogleMobileAds|play-services-ads|google_mobile_ads|applovin|unity-ads|ironsource":
        ("reklam", "Reklam SDK'sı: rıza/ATT + yurt dışı aktarım."),
    r"stripe\.com|js\.stripe|paypal|braintree":
        ("odeme", "Yurt dışı ödeme sağlayıcısı: veri işleyen/aktarım değerlendirmesi."),
}

LLM = re.compile(r"api\.openai\.com|api\.anthropic\.com|generativelanguage\.googleapis\.com|"
                 r"api\.mistral\.ai|api\.cohere\.|openrouter\.ai|from openai|import openai|"
                 r"@anthropic-ai/sdk|import anthropic", re.I)
PRECHECKED = re.compile(r"""(<input[^>]*type=["']checkbox["'][^>]*\bchecked\b)|defaultChecked(?:=\{?true\}?)?|"""
                        r"""(?:isOn|isChecked|consent\w*|marketing\w*|newsletter\w*)\s*[:=]\s*true""", re.I)
LOG_PII = re.compile(
    r"(console\.log|logger\.\w+|log\.\w+|print|println|NSLog|Log\.[dviwe]|os_log)\s*\(.*"
    r"(email|e-posta|eposta|phone|telefon|tckn|tc_?kimlik|password|şifre|sifre|token|iban|card|kart)", re.I)
TCKN = re.compile(r"\b[1-9][0-9]{10}\b")
URL = re.compile(r"""(?:https?:)?//([A-Za-z0-9.-]+)([/A-Za-z0-9._~:?#@!$&'()*+,;=%-]*)""")


def iter_files(root):
    for d, dirs, files in os.walk(root):
        dirs[:] = [x for x in dirs if x not in SKIP_DIRS]
        for f in files:
            p = os.path.join(d, f)
            if os.path.splitext(f)[1].lower() in EXTS and os.path.getsize(p) <= MAX_BYTES:
                yield p


def scan(root):
    findings = []

    def add(kind, path, line, msg, text):
        findings.append({"tur": kind, "dosya": os.path.relpath(path, root), "satir": line,
                         "not": msg, "ornek": text.strip()[:160]})

    for p in iter_files(root):
        try:
            with open(p, encoding="utf-8", errors="ignore") as fh:
                lines = fh.read().splitlines()
        except OSError:
            continue
        for i, line in enumerate(lines, 1):
            low = line.lower()
            for m in URL.finditer(line):
                full = (m.group(1) + m.group(2)).lower()
                for host, (kind, msg) in REMOTE_HOSTS.items():
                    if full.startswith(host) or m.group(1).lower() == host:
                        add(kind, p, i, msg, line)
            for pat, (kind, msg) in TRACKERS.items():
                if re.search(pat, line, re.I):
                    add(kind, p, i, msg, line)
            if LLM.search(line):
                add("llm", p, i, "LLM API: kişisel veri gönderiliyorsa yurt dışı aktarım + işleyen sözleşmesi + aydınlatma.", line)
            if PRECHECKED.search(line) and ("checkbox" in low or "consent" in low or "izin" in low
                                            or "onay" in low or "ischecked" in low or "ison" in low
                                            or "marketing" in low or "newsletter" in low):
                add("onceden-isaretli", p, i, "Önceden işaretli onay/rıza: açık rıza değildir.", line)
            if LOG_PII.search(line):
                add("log-pii", p, i, "Log satırında olası kişisel veri; maskeleyin/çıkarın.", line)
            if TCKN.search(line) and ("tc" in low or "kimlik" in low or "tckn" in low):
                add("tckn", p, i, "T.C. kimlik no benzeri değer/alan: gereksizse toplamayın, saklıyorsanız şifreleyin.", line)
    return findings


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(2)
    root = os.path.abspath(sys.argv[1])
    out = scan(root)
    if "--json" in sys.argv:
        print(json.dumps(out, ensure_ascii=False, indent=2))
        return
    by = {}
    for f in out:
        by.setdefault(f["tur"], []).append(f)
    for kind in sorted(by):
        print(f"\n== {kind} ({len(by[kind])}) ==")
        for f in by[kind]:
            print(f"{f['dosya']}:{f['satir']}  {f['not']}\n    {f['ornek']}")
    print(f"\nToplam bulgu: {len(out)} (manuel doğrulama gerekir; hüküm değildir)")


if __name__ == "__main__":
    main()
