# VERBİS, ETBİS, İYS ve e-ticaret kimlik bilgileri

## VERBİS (6698 m.16)
Kaynak: Kurul kararları 04.09.2025/2025/1572 ve 25.12.2025/2025/2393, kvkk.gov.tr kamuoyu duyuruları (D).
- **Genel muafiyet:** yıllık çalışan sayısı 50'den az **ve** yıllık mali bilanço toplamı 100 milyon TL'den az, ana faaliyeti özel nitelikli veri işleme olmayan sorumlular.
- **Ana faaliyet özel nitelikli veri işleme** ise: çalışan 10'dan az **ve** bilanço 10 milyon TL'den az olanlar muaf.
- 2025/2393: bilanço esasına göre defter tutanlarda iki kriter birlikte; bilanço esasına göre defter **tutmayanlarda yalnızca çalışan sayısı**.
- Muafiyet yalnız sicile kayıt muafiyetidir; aydınlatma, güvenlik, silme vb. yükümlülükler sürer.
- Ceza (2026): 341.809–17.092.242 TL.
- Eski "25 milyon TL" eşiği **geçersiz**. Yurt dışında yerleşik sorumlular için ayrıca temsilci/kayıt kuralları var (kvkk.gov.tr'den kontrol et).
- Karar metninin kendisi (RG) okunmadı; duyuru üzerinden doğrulandı → kayıt yükümlülüğü sınırda ise kvkk.gov.tr'yi ve avukatı kontrol et.

## ETBİS (6563)
Kaynak: ticaret.gov.tr/duyurular (D).
- ETBİS kaydı için **ciro/hacim eşiği yok**: elektronik ticaret hizmet sağlayıcılar ve aracı hizmet sağlayıcılar faaliyete başlamadan önce kayıt olur, değişiklikler 30 gün içinde bildirilir.
- 6563'teki 10/30/60 milyar TL tutarları büyük aracı hizmet sağlayıcıların ölçek/lisans kademeleridir; küçük geliştirici için genellikle ilgisizdir (güncel tutarlar doğrulanamadı).
- Ceza (2026, RG 25.12.2025/33118; tutarlar düşük çözünürlüklü görselden okundu, K): ETBİS bildirim/belge sunmama 143.102–715.516 TL.
- Kendi ürün/hizmetini kendi sitesi/uygulamasında satan "hizmet sağlayıcı" da kapsama girebilir; mali müşavir/avukatla teyit et.

## 6563 — site/uygulamada bulunacak bilgiler (K)
Ticari unvan veya marka, MERSİS (esnafta VKN), KEP/iletişim, merkez adresi, telefon, ticaret sicil bilgisi vb. kolay erişilir olmalı. Yönetmelik madde metni okunamadı → ticaret.gov.tr mevzuat sayfasından kontrol et. Uygulama içinde "Hakkımızda/İletişim/Satıcı Bilgisi" ekranı ekle.

## Ticari elektronik ileti ve İYS (K)
- SMS, e-posta, arama ile ticari ileti için alıcıdan **önceden onay**; ret hakkı her zaman. Tacir/esnaf alıcılarda ön onay şartı yok, ret hakkı var.
- İYS kaydı hizmet sağlayıcıya ait (e-Devlet/e-imza); onay/ret kayıtları İYS'de tutulur.
- **İYS onayı KVKK sorumluluğunu karşılamaz:** iki ayrı rejim. 6563 m.6/m.11(5) (D) ve Yönetmelik m.12–13 (onay kayıtları 3 yıl, ispat yükü hizmet sağlayıcıda; ikincil, K). KVKK Kurulu 2022/107: ticari ileti ayrı mevzuata tabi olsa da numara kişisel veridir; ilişki veya açık rıza kanıtı olmadan gönderim m.12 ihlali, 75.000 TL (D, karar özeti). 2018/119 İlke Kararı: rıza veya m.5(2) şartı olmadan reklam SMS/arama/e-posta durdurulmalı. Kurul'dan "İYS onayı açık rızanın yerini tutar/tutmaz" diyen açık hüküm bulunamadı (X); pratik: ikisini birlikte yürüt.
- Ceza (2026, ikincil): ticari ileti ve bilgi yükümlülükleri 2.859–42.930 TL aralığında kalemlere göre (RG 25.12.2025/33118).
- Teknik: ret/çıkış bağlantısı her iletide; çıkış anında gönderimi durdur; onay kaynağı ve zamanını sakla.

## Araç kontrolü
audit.py şunları işaretler: e-posta/SMS SDK'ları (Mailchimp, SendGrid vb. eklenmeli), önceden işaretli pazarlama onayı. Sonuçları bu dosyayla birlikte raporla.
