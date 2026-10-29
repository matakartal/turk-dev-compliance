// Log, hata izleme (Sentry vb.) ve APM'e giden olaylardan kişisel veriyi maskele.
// Kullanım: logger.format'a ve Sentry beforeSend'e bağla.

const EMAIL = /[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}/gi;
const PHONE = /(?:\+?90|0)?\s?5\d{2}\s?\d{3}\s?\d{2}\s?\d{2}/g;
const TCKN = /\b[1-9]\d{10}\b/g;
const IBAN = /\bTR\d{2}\s?(?:\d{4}\s?){5}\d{2}\b/gi;
const PAN = /\b(?:\d[ -]?){13,19}\b/g; // kart numarası benzeri (Luhn ile doğrula)
const SENSITIVE_KEYS = /^(password|pass|sifre|şifre|token|authorization|cookie|cvv|cvc|card|kart|tckn|iban|secret)$/i;

function luhn(num: string): boolean {
  const d = num.replace(/\D/g, "");
  if (d.length < 13 || d.length > 19) return false;
  let sum = 0;
  for (let i = 0; i < d.length; i++) {
    let n = +d[d.length - 1 - i];
    if (i % 2) { n *= 2; if (n > 9) n -= 9; }
    sum += n;
  }
  return sum % 10 === 0;
}

export function maskString(s: string): string {
  return s
    .replace(EMAIL, "[email]")
    .replace(PHONE, "[tel]")
    .replace(IBAN, "[iban]")
    .replace(PAN, (m) => (luhn(m) ? "[kart]" : m))
    .replace(TCKN, "[tckn]");
}

export function maskDeep<T>(v: T, depth = 0): T {
  if (depth > 6) return v;
  if (typeof v === "string") return maskString(v) as unknown as T;
  if (Array.isArray(v)) return v.map((x) => maskDeep(x, depth + 1)) as unknown as T;
  if (v && typeof v === "object") {
    const out: Record<string, unknown> = {};
    for (const [k, val] of Object.entries(v as Record<string, unknown>)) {
      out[k] = SENSITIVE_KEYS.test(k) ? "[gizli]" : maskDeep(val, depth + 1);
    }
    return out as T;
  }
  return v;
}

// Sentry örneği:
// Sentry.init({ beforeSend: (e) => maskDeep(e), sendDefaultPii: false });
