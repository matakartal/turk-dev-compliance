# turk-dev-compliance

Türkiye'de uygulama, site veya SaaS yapan geliştiriciler için açık kaynak bir **Agent Skill** (`SKILL.md` formatı). KVKK ve çevresindeki mevzuatı kod ve tasarım üzerinde kontrol eder, taslak metin üretir, kod kalıbı verir.

> **Hukuki tavsiye değildir.** Bkz. [DISCLAIMER.md](DISCLAIMER.md). Her kural kaynağı ve doğrulama durumuyla birlikte gelir (`references/guncellik.md`).

*(English: an open-source Agent Skill that helps developers shipping apps/sites to Turkish users with KVKK (Turkish GDPR-like law) and related rules: consent vs. notice, cookies, cross-border transfer incl. remote fonts/CDNs/SDKs, VERBİS, distance-sales checkout, minors, store policies. Turkish-first, MIT. Not legal advice.)*

## Ne yapar?
- **İncele:** `scripts/audit.py` ile projeyi tarar (uzak font/CDN/embed, izleyici ve reklam SDK'ları, önceden işaretli rıza, log'da kişisel veri, LLM API çağrıları), bulguları kural ve kaynakla eşleştirip raporlar.
- **Şablon üret:** aydınlatma, açık rıza, çerez politikası, saklama-imha, ön bilgilendirme formu, mesafeli satış sözleşmesi, ihlal planı, başvuru yanıtı. Kısa sorular sorar, kopyala-yapıştır yerine **sana özel** taslak yazar (Kurul 2026/347).
- **Kod kalıbı:** rıza kaydı (SQL), çerez kapısı, ilgili kişi başvurusu, log maskeleme, checkout bileşeni.

## Kapsam
KVKK temel çerçeve · aydınlatma ≠ açık rıza (2026/347) · çerez rehberi (2025) · yurt dışı aktarım ve standart sözleşme · uzak font/CDN (Google Fonts) · VERBİS/ETBİS/İYS · mesafeli satış ve checkout · abonelik · ödeme/fatura/vergi notları · çocuk ve yaş doğrulama (7578, 5651) · App Store / Google Play · veri ihlali (72 saat) · yapay zekâ/LLM.

## Kurulum
Claude Code:
```bash
git clone https://github.com/matakartal/turk-dev-compliance.git
cp -R turk-dev-compliance/skills/turk-dev-compliance ~/.claude/skills/
```
Proje bazlı için `.claude/skills/` altına kopyala. Sonra Claude'a "bu projeyi KVKK açısından incele" veya "aydınlatma metni hazırla" de.

Scripti tek başına da çalıştırabilirsin:
```bash
python3 skills/turk-dev-compliance/scripts/audit.py ./projem
```

## Güvenilirlik politikası
Durum etiketleri: **D** doğrulandı (birincil metin okundu) · **K** kısmen (ikincil kaynak) · **X** doğrulanamadı. Örneğin KVKK'nın Google Fonts için bir kararı **yoktur/bulunamadı**; skill bunu "zorunlu" diye sunmaz, risk azaltma (self-host) olarak önerir. Son doğrulama: 2026-10-29. Ham araştırma notları: [`research/`](research/).

## Test
```bash
python3 evals/run.py
```
Örnek projelerde (`evals/`) audit çıktısının beklenen bulgu türleriyle eşleştiğini doğrular.

## Katkı
Hukuki içerik PR'ları **birincil kaynak linki** ve doğrulama tarihi içermeli. Bkz. [CONTRIBUTING.md](CONTRIBUTING.md). Avukat/mali müşavir gözden geçirmesi özellikle değerlidir; `v1.0` bir uzman incelemesinden önce etiketlenmez.

## Lisans
MIT — [LICENSE](LICENSE).
