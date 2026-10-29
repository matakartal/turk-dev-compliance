// Rıza öncesi izleyici yükleme kapısı (KVKK Çerez Rehberi 2025).
// - Zorunlu olmayan script'ler rıza verilene kadar DOM'a hiç eklenmez.
// - Varsayılan: tüm isteğe bağlı kategoriler KAPALI (ön işaretli değil).
// - Kabul / Reddet / Tercihler eşit görünürlükte olmalı (UI tarafı).
// - Rıza sürümü değişirse tekrar sorulur.

export type Category = "analytics" | "marketing";
type Consent = { v: number; at: string; choices: Record<Category, boolean> };

const CONSENT_VERSION = 1;
const KEY = "cookie_consent";
const DEFAULT: Record<Category, boolean> = { analytics: false, marketing: false };

export function readConsent(): Consent | null {
  try {
    const raw = document.cookie.split("; ").find((c) => c.startsWith(KEY + "="));
    if (!raw) return null;
    const c = JSON.parse(decodeURIComponent(raw.slice(KEY.length + 1))) as Consent;
    return c.v === CONSENT_VERSION ? c : null; // sürüm değiştiyse yeniden sor
  } catch {
    return null;
  }
}

export function saveConsent(choices: Partial<Record<Category, boolean>>) {
  const c: Consent = {
    v: CONSENT_VERSION,
    at: new Date().toISOString(),
    choices: { ...DEFAULT, ...choices },
  };
  // Tercih çerezi "zorunlu" kategoridedir; süreyi orantılı tut (6 ay).
  document.cookie = `${KEY}=${encodeURIComponent(JSON.stringify(c))}; Max-Age=${60 * 60 * 24 * 180}; Path=/; SameSite=Lax; Secure`;
  applyConsent(c);
  // Sunucuya ispat kaydı gönder (snippets/consent-log.sql)
  void fetch("/api/consent", { method: "POST", headers: { "content-type": "application/json" }, body: JSON.stringify(c) });
}

const loaders: Record<Category, () => void> = {
  analytics: () => loadScript("/vendor/analytics.js"), // kendi origin'inden servis et
  marketing: () => {
    /* örn. Meta Pixel — yalnızca rıza sonrası */
  },
};
const loaded = new Set<Category>();

export function applyConsent(c: Consent | null) {
  if (!c) return; // karar yok = hiçbir isteğe bağlı script yok
  (Object.keys(c.choices) as Category[]).forEach((k) => {
    if (c.choices[k] && !loaded.has(k)) {
      loaders[k]();
      loaded.add(k);
    }
  });
  // Rıza geri alındıysa: script'i bir sonraki sayfa yüklemesinde yükleme; çerezleri temizle.
}

function loadScript(src: string) {
  const s = document.createElement("script");
  s.src = src;
  s.async = true;
  document.head.appendChild(s);
}

// Başlangıç
applyConsent(readConsent());
