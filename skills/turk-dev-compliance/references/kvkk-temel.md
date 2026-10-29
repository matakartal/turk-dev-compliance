# KVKK temel çerçeve (6698)

Kaynak: 6698 sayılı Kanun, mevzuat.gov.tr/MevzuatMetin/1.5.6698.pdf (7499 ile son değişiklik 01.06.2024). Madde numaraları kanun metnine göredir; bu dosya özet niteliğindedir.

## Roller
- **Veri sorumlusu:** amaçları ve vasıtaları belirleyen (genelde uygulamayı yayımlayan şirket/kişi).
- **Veri işleyen:** sorumlunun yetkisiyle adına işleyen (barındırma, analitik, e-posta servisi, ödeme PSP'si çoğunlukla). İşleyenle yazılı **veri işleme sözleşmesi** yap.
- Müşterinin verisini işleyen B2B SaaS'ta sen **işleyen**, müşterin sorumludur; kendi kullanıcı hesapların için sorumlusun.

## İlkeler (m.4)
Hukuka ve dürüstlük kurallarına uygunluk, doğruluk ve güncellik, belirli-açık-meşru amaç, amaçla bağlantılı sınırlı ve ölçülü işleme, gerekli süre kadar saklama.

## İşleme şartları (m.5) — özet
Açık rıza; kanunda açıkça öngörülme; fiili imkânsızlık; sözleşmenin kurulması/ifası için gerekli olması; hukuki yükümlülük; ilgili kişinin alenileştirmesi; hakkın tesisi/kullanımı/korunması; meşru menfaat (temel haklara zarar vermemek şartıyla). **Mümkünse rıza dışındaki şartı kullan**; rızayı geri alınabilirliği ve ispat yükü nedeniyle son çare yap. Yanlış şart etiketi (ör. sözleşme gerekliyken "rıza") hata sayılır.

## Özel nitelikli veri (m.6)
Irk, etnik köken, siyasi düşünce, felsefi inanç, din/mezhep, kılık-kıyafet, dernek/vakıf/sendika üyeliği, sağlık, cinsel hayat, ceza mahkûmiyeti/güvenlik tedbirleri, **biyometrik ve genetik veri**. 7499 ile işleme şartları yeniden yazıldı (GDPR'a yaklaştırıldı). Sağlık/biyometrik/dini inanç verisi toplayan uygulamada hukuki sebep ve güvenlik tedbirini yazılı çıkar; VERBİS muafiyet eşikleri de buna bağlı değişir.

## Silme, yok etme, anonimleştirme (m.7)
İşleme şartları ortadan kalkınca silinir/yok edilir/anonimleştirilir. Saklama-imha politikası ve periyodik imha (6 ay) için Yönetmelik hükümleri geçerlidir (kvkk.gov.tr'den güncel metni kontrol et). Şablon: `templates/saklama-imha.md`.

## Aydınlatma (m.10) ve haklar (m.11, m.13)
Aydınlatma: kimlik, amaç, aktarılan alıcılar ve amaç, toplama yöntemi ve hukuki sebep, 11. madde hakları. İlgili kişi hakları: öğrenme, bilgi talep, amaç/uygun kullanım, aktarılan üçüncü kişileri bilme, düzeltme, silme/yok etme, üçüncü kişilere bildirim, otomatik analizle aleyhe sonuca itiraz, zararın giderilmesi. Başvuru en geç **30 gün** içinde cevaplanır (m.13). Şablon: `templates/basvuru-yaniti.md`; kod: `snippets/dsar-endpoint.ts`.

## Güvenlik (m.12)
Hukuka aykırı işlemeyi/erişimi önleme, muhafaza için uygun güvenlik düzeyi, tedbirlerin alınması ve denetimi; işleyen de sorumlu. Yetkisiz elde edilmede en kısa sürede (Kurul kararıyla **72 saat**) bildirim (bkz. `guvenlik-ihlal.md`).

## Yaptırım (m.18) — 2026 tutarları (TL, alt–üst)
- Aydınlatma yükümlülüğü: 85.437–1.709.200
- Veri güvenliği: 256.357–17.092.242
- Kurul kararına uymama: 427.263–17.092.242
- VERBİS yükümlülüğü: 341.809–17.092.242
- Standart sözleşme bildirimi: 90.308–1.806.177
Tutarlar her yıl yeniden değerleme oranıyla değişir; kaynak kvkk.gov.tr/Icerik/8145. Kurul cezalarına idare mahkemesinde dava açılır.

## Ağırlıklı kurallar için sırayla
`aydinlatma-riza.md` → `cerez.md` → `yurt-disi-aktarim.md` → `verbis-etbis-iys.md` → `guvenlik-ihlal.md`.
