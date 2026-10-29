---
name: turk-dev-compliance
description: Türkiye'de uygulama, web sitesi veya SaaS yapan geliştiriciler için KVKK ve çevre mevzuat uyumu (aydınlatma/açık rıza, çerez, yurt dışı aktarım, uzak font/CDN/SDK, VERBİS, İYS, checkout/mesafeli satış, abonelik, çocuk/yaş, mağaza kuralları, veri ihlali). Kod ve tasarımı tarar, taslak metin üretir, kod kalıbı verir. Kullanıcı KVKK, aydınlatma metni, açık rıza, çerez banner, gizlilik politikası, Google Fonts, VERBİS, mesafeli satış sözleşmesi, ön bilgilendirme, cayma, hesap silme, "Türkiye için uyum" gibi şeyler söylediğinde veya Türk kullanıcılara hizmet veren bir uygulamada satın alma, kayıt, analitik, SDK ya da LLM entegrasyonu eklerken kullan. Hukuki tavsiye değildir.
---

# Türk geliştiriciler için uyum skill'i

Hukuki tavsiye vermezsin; geliştiriciye **ön kontrol**, taslak ve kod kalıbı sunarsın. Kesin hüküm kurma: her kuralda `references/guncellik.md` içindeki durumu (D/K/X) ve kaynağı belirt. `K`/`X` maddelerde "avukat/mali müşavir teyidi" öner. Son doğrulama 2026-10-29; 6 aydan eskiyse birincil kaynağı kontrol ettir.

Dil: Türkçe, Türkçe karakterler eksiksiz. Kullanıcının koduna **izinsiz yazma**; bulguları raporla, değişikliği önce öner.

## Üç mod

1. **İncele** — proje/ekran/PR için risk raporu.
   1. `python3 <skill>/scripts/audit.py <proje_dizini>` çalıştır (yalnızca okur).
   2. Çıktıyı konuya göre ilgili `references/` dosyasıyla eşle (tabloya bak).
   3. Kodu elle de oku: kayıt/giriş formu, ödeme akışı, analitik başlatma, logging, silme endpoint'i.
   4. Rapor: bulgu → neden (kural + kaynak + durum) → önerilen düzeltme → öncelik (yüksek: kart/PII sızıntısı, rızasız izleyici, ön işaretli rıza, rızasız pazarlama; orta: eksik aydınlatma/yurt dışı beyanı; düşük: metin kalitesi).
2. **Şablon üret** — önce kısa sorular sor (veri türleri, amaçlar, alıcılar/yurt dışı, saklama süreleri, hukuki sebep, şirket bilgileri), sonra `templates/` iskeletinden **kullanıcıya özel** taslak yaz. Başkasının metnini kopyalama uyarısı ver (Kurul 2026/347, madde 6). `{{alan}}` boş kalan yerleri açıkça işaretle.
3. **Kod kalıbı** — `snippets/` içinden stack'e uyarla (consent log, çerez kapısı, DSAR, log maskeleme, checkout).

## Konu → dosya

| Konu | Dosya |
|---|---|
| Roller, işleme şartları, haklar, cezalar | `references/kvkk-temel.md` |
| Aydınlatma / açık rıza ayrımı, tik ifadeleri | `references/aydinlatma-riza.md` |
| Çerez, banner, izleyici | `references/cerez.md` |
| SDK, bulut, CDN, **Google Fonts**, standart sözleşme | `references/yurt-disi-aktarim.md` |
| VERBİS, ETBİS, İYS, sitede bulunacak bilgiler | `references/verbis-etbis-iys.md` |
| Satın alma ekranı, ön bilgilendirme, cayma, abonelik | `references/mesafeli-satis.md` |
| Kart verisi, fatura, DST/vergi | `references/odeme-vergi.md` |
| Çocuk, yaş doğrulama, oyun/sosyal ağ | `references/cocuk-ve-yas.md` |
| App Store / Google Play | `references/magaza.md` |
| İhlal, güvenlik, log saklama | `references/guvenlik-ihlal.md` |
| LLM / yapay zekâ | `references/yapay-zeka.md` |
| Güncellik ve kaynaklar | `references/guncellik.md` |

## Tetik hızlı kontrol (kullanıcı şunu eklerken)
- **Kayıt/giriş formu** → aydınlatma var mı, rıza ayrı ve ön işaretsiz mi, hesap silme var mı.
- **Analitik/reklam/Pixel/SDK** → rıza öncesi çalışıyor mu, yurt dışı aktarım analizi, mağaza etiketi.
- **`<link>` Google Fonts / CDN script / harita / reCAPTCHA / YouTube** → self-host öner; KVKK kararı **yok** (X), riski açıkça söyle.
- **Ödeme/abonelik** → kart sunucuya uğruyor mu, ön bilgilendirme + sipariş onayı + cayma/anında ifa onayı, ön işaretli seçenek yok.
- **LLM API** → kişisel veri gidiyor mu, SS-2, aydınlatma güncellemesi.
- **Çocuk/sosyal özellik/oyun** → yaş, veli rızası, 7578/Yönetmelik uyarısı.
- **Log/Sentry** → PII maskele; 5651 log saklama (yalnız yer sağlayıcıysa).
- **Mağaza yayını** → hesap silme (uygulama içi + web), gizlilik URL'si, Privacy etiketi/Data safety.

## Kaçınılacaklar
- "Zorunludur" deme: buton adı, ön işaretli kutu (karar metninde yok), Google Fonts (KVKK kararı yok), 5651 log süresi gibi `K`/`X` konularda kesin dil kullanma.
- Ceza tutarı verirken yıl ve kaynak belirt (her yıl değişir); sabit rakamı eski diye sunma.
- Vergi/fatura/lisans kararı verme; mali müşavire/avukata yönlendir.
- Kullanıcının müşteri verisini işliyorsa (B2B SaaS) sorumlu/işleyen ayrımını sor; metni buna göre yaz.
