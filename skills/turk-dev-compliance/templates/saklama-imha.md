<!--
TASLAK — Saklama ve İmha Politikası iskeleti. Süreleri mevzuata ve kendi ihtiyacına göre doldur. Güncel yasal gereklilikleri (saklama süreleri, periyodik imha aralığı) kvkk.gov.tr / mevzuat.gov.tr'den ve mali müşavirden teyit et.
-->

# Kişisel Verileri Saklama ve İmha Politikası

**Sorumlu:** {{ad / rol}}  **Sürüm:** {{1.0}}  **Tarih:** {{...}}

## Veri envanteri ve süreler
| Veri / kayıt | Amaç | Hukuki sebep | Saklama süresi | Süre sonu işlemi | Yer |
|---|---|---|---|---|---|
| Hesap bilgileri | Üyelik | Sözleşme | Üyelik + {{1 yıl}} | Silme | {{DB}} |
| Fatura/sipariş | Vergi | Yasal yükümlülük | {{10 yıl — mali müşavirle teyit}} | Silme/imha | {{DB}} |
| Pazarlama rızası kaydı | İspat | Meşru menfaat/ispat | Rıza + {{süre}} | Silme | {{DB}} |
| Uygulama logları | Güvenlik | Meşru menfaat | {{30–90 gün}} | Otomatik silme | {{log}} |
| Trafik logları (5651, yalnız yer sağlayıcıysanız) | Yasal | Kanun | {{1–2 yıl; avukatla teyit}} | İmza + silme | {{ayrı depo}} |
| Destek yazışmaları | Destek | Meşru menfaat | {{2 yıl}} | Silme | {{...}} |

## Yöntem
- **Silme:** veritabanından kalıcı silme; yedeklerde {{yedek döngüsü}} sonunda yok olur.
- **Yok etme:** fiziksel medyada geri döndürülemez imha.
- **Anonimleştirme:** kimlikle ilişkilendirilemeyecek şekilde (sadece takma ad/hash yeterli sayılmaz).
- **Periyodik imha:** {{6 ay}} aralıkla kontrol; kayıt tutulur (tarih, kapsam, yöntem, sorumlu).
- Hesap silme talebinde {{30 gün}} içinde işlem; yasal saklama gerektiren kayıtlar süre sonuna kadar ayrı ve kısıtlı tutulur.

## Sorumluluk ve kayıt
İmha kayıtları {{saklama süresi}} tutulur. İşleyenler de politikaya bağlıdır (sözleşme).
