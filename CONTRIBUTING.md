# Katkı rehberi

## Hukuki içerik
- Her kural: **kaynak URL** (mümkünse kvkk.gov.tr, resmigazete.gov.tr, mevzuat.gov.tr), **tarih** ve durum etiketi (D/K/X). `references/guncellik.md` tablosunu güncelle.
- Kural cümlelerini **kendi cümlenle** özetle; uzun alıntı yapma. Başka bir skill/blogun metnini kopyalama (lisans ve Kurul 2026/347 madde 6).
- Yorum ile kural ayrı yazılır: "(yorum)" / "(ikincil)" ifadeleri koru.
- Ceza tutarı ekliyorsan yıl ve kaynak yaz.
- Emin olmadığın şeyi `X` yaz; uydurma kesinlik ekleme.

## Kod
- `scripts/audit.py` yalnızca **okur**, bağımlılığı olmaz (stdlib).
- Yeni tespit eklersen `evals/` altına örnek ve `expected.json` ekle; `python3 evals/run.py` geçmeli.
- TypeScript snippet'leri `tsc --strict` ile derlenmeli.

## Dil
Türkçe, tüm Türkçe karakterlerle. Teknik terimler ve kod orijinal kalır.
