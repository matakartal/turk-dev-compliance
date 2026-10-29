# Ticaret, Vergi ve Ödeme Araştırması (Türkiye, uygulama/e-ticaret geliştiricisi)

Tarih: 2026-10-29

Yöntem notu: Arama motoru çıktısı ağırlıkla ikincil kaynak döndürdü. resmigazete.gov.tr, mevzuat.gov.tr, gib.gov.tr ve iys.org.tr üzerindeki PDF veya tam metinler araçla okunamadı (ham PDF veya 403). Bu yüzden "doğrulandı" yalnızca birden fazla bağımsız kaynakta tutarlı ve resmi künye (RG sayı/tarih) içeren maddelere verildi. Ham metin görülmediyse "kısmen" yazıldı. Kaynak türü: birincil = resmi kurum sitesi; ikincil = mevzuat derleme sitesi, hukuk bürosu, haber veya blog. Üretime almadan önce her madde için RG metni mevzuat.gov.tr üzerinden kontrol edilmeli. Bu belge hukuki görüş değildir.

---

## 1) Mesafeli Sözleşmeler Yönetmeliği (RG 27.11.2014/29188)

### 1.1 Değişiklik zinciri ve 2025-2026
- Kural: 24.05.2025 tarihli RG (32909) ile değişiklik yayımlandı. Madde 5/1 (g) ve (k) (cayma ve iade taşıyıcısı bilgisi, hakem heyeti/arabuluculuk bilgisi) yeniden yazıldı. Madde 12'de satıcının belirttiği taşıyıcı ile yapılan iade masrafı tüketiciye yüklenemiyor. Ön bilgilendirmede taşıyıcı belirtilmemişse iade bedeli talep edilemiyor. Platform satışında bilgi eksikliği veya şube yokluğu aracı hizmet sağlayıcıdan kaynaklanıyorsa masraf ona ait. Madde 13/3 ve 15/1(i) yürürlükten kaldırıldı. Yönetmelik hükümleri 01.01.2026'da yürürlüğe girdi. 10.08.2024 değişikliği ise Geçici Madde 1 tarihini 01.01.2025'ten 01.01.2026'ya ertelemişti.
- Kaynak: https://www.resmigazete.gov.tr/fihrist?tarih=2025-05-24 (birincil, fihrist; madde ayrıntısı okunamadı); madde özeti https://www.alomaliye.com/2025/05/24/mesafeli-sozlesmeler-yonetmeliginde-degisiklik-24-05-2025/amp/ ; 2024 erteleme: https://www.alomaliye.com/2024/08/10/mesafeli-sozlesmeler-yonetmeliginde-degisiklik-10-08-2024/amp/
- Kaynak türü: birincil (RG fihrist, yalnızca künye) + ikincil (alomaliye madde özeti)
- Doğrulama: kısmen (künye ve yürürlük tarihi tutarlı; resmi metin görülmedi)

### 1.2 Ön bilgilendirme formu ve sipariş onayı / buton ifadesi
- Kural: Madde 8'e göre satıcı/sağlayıcı/aracı, siparişi onaylatmadan hemen önce siparişin ödeme yükümlülüğü doğurduğunu açık ve anlaşılır bildirmeli. Bildirim yapılmazsa tüketici siparişle bağlı olmaz. Derlenmiş metinde butonda kullanılacak sabit bir ifade zorunluluğu görülmedi. Zorunluluk içerik ve zamanlamaya ilişkin (sözleşmeden önce, ödeme yükümlülüğünden hemen önce). Pratikte "Siparişi onayla / Ödeme yapmakla yükümlü olduğunuzu kabul ediyorum" benzeri açık ifade önerilir, ama kanuni sabit metin yok. Ön bilgilendirme formu için 2025 değişikliği sadece cayma/iade taşıyıcısı ve uyuşmazlık başvuru bilgisini güncelliyor.
- Kaynak: https://www.lexpera.com.tr/mevzuat/yonetmelikler/mesafeli-sozlesmeler-yonetmeligi ; https://ticaret.gov.tr/haberler/internet-ve-telefon-vasitasiyla-yapilan-satislara-yeni-standartlar-geldi
- Kaynak türü: ikincil (lexpera derlemesi); ticaret.gov.tr haberi birincil ama içeriği okunmadı
- Doğrulama: kısmen

### 1.3 Dijital içerik / anlık ifa / IAP için cayma
- Kural: Madde 15/1 (ğ): elektronik ortamda anında ifa edilen hizmetler ve tüketiciye anında teslim edilen gayrimaddi mallarda cayma hakkı yok. (e): ambalajı açılmış dijital içerik/kitap/sarf malzemesi benzeri. Aynı sayfada (k) kurulum/montaj bendi ile (ı) ve (j) bentleri için Danıştay iptal notu var (6/5/2026 tarihli karar); bu not tek derleme sitesinden geliyor, ayrıca teyit gerekir. 6502 sayılı Kanun m.48/5 cayma süresi 14 gündür ve dijital içerikte tüketicinin onayıyla ifaya başlanması hakkı sonlandırır; ön bilgilendirmede bu açıkça yer almalı. Apple/Google IAP işlemlerinde satıcı fiilen mağaza olduğundan iade/cayma mağaza politikasıyla yürür; geliştirici yine de kendi sitesindeki satışlarda yukarıdaki kurallara tabidir (son cümle ikincil yorum, doğrulanmadı).
- Kaynak: https://www.lexpera.com.tr/mevzuat/yonetmelikler/mesafeli-sozlesmeler-yonetmeligi
- Kaynak türü: ikincil
- Doğrulama: kısmen (m.15 maddeleri tutarlı; Danıştay iptal notu ve IAP yorumu doğrulanamadı)

---

## 2) Abonelik Sözleşmeleri Yönetmeliği ve 6502 m.52

### 2.1 Mevcut kural çerçevesi
- Kural: 6502 m.52 ve Abonelik Sözleşmeleri Yönetmeliği kapsamında abonelik fesih talebinin sağlayıcıya ulaşmasından itibaren belirli sürede (kaynaklara göre 7 gün) yerine getirilmesi, fesih kanallarının abonelik kanalından daha zor olmaması ve bilgilendirme yükümlülükleri geçerli. Tek tıkla fesih ve otomatik yenileme ayrıntıları madde bazında doğrulanamadı.
- Kaynak: https://www.erdem-erdem.av.tr/bilgi-bankasi/abonelik-sozlesmelerinin-sona-erdirilmesi ; https://bilalalyar.av.tr/?p=101463
- Kaynak türü: ikincil
- Doğrulama: kısmen (7 gün süresi tek kaynaktan; Yönetmelik metni okunamadı)

### 2.2 Ticaret Bakanlığı dijital abonelik düzenleme çalışması (son durum)
- Kural: Ekim 2026 itibarıyla Ticaret Bakanı Ömer Bolat'ın TBMM yazılı soru yanıtında abonelik mevzuatını güncelleme çalışması başladığı bildirildi; büyük hizmet sağlayıcılar inceleniyor, rapor hazırlanıyor. Henüz yayımlanmış yönetmelik, taslak veya yürürlük tarihi yok. "Tüm otomatik yenilemeler yasaklanıyor" veya "toplu yeniden onay" yönünde kesin karar haberlerde doğrulanmadı. 2025-2026 dijital abonelik başvuru sayısı 1.459, otomatik yenileme başvuruları 282 (2023-2026, dönemler farklı). Örnek ceza 2022'de 5.946.435 TL (onaysız yenileme, 9.669 tüketici). Ayrıca BTK'nın elektronik haberleşme tüketici hakları yönetmeliği 11.06.2026 RG (33277) ile değişti, 25.06.2026'da yürürlüğe girdi; bu telekom abonelikleriyle ilgili, dijital uygulama aboneliklerini kapsamıyor.
- Kaynak: https://www.dunya.com/ekonomi/dijital-aboneliklerde-onaysiz-yenileme-mercek-altinda-bakanlik-inceleme-baslatti-haberi-844536 ; https://www.alomaliye.com/2026/06/11/elektronik-haberlesmede-tuketici-haklari-yonetmeligi-degisti-kapsamli-ozet/
- Kaynak türü: ikincil (haber)
- Doğrulama: kısmen (düzenleme yok olduğu birden çok haberde tutarlı; Bakanlık yanıtı birincil kaynaktan görülmedi)

Geliştirici pratiği: onay olmadan yenileme, iptal yolunun kayıttan zor olması ve yenileme öncesi hatırlatma eksikliği idari para cezası riski; kural değişmeden önce bile uyumlu tasarım önerilir (iptal akışı uygulama içinde, yenileme öncesi bildirim). Bu, kaynaktan doğrulanmış kural değil, tasarım önerisidir.

---

## 3) 6563 sayılı Kanun (7416 ile değişik) ve Yönetmelik

### 3.1 Sitede bulunması gereken bilgiler
- Kural: Hizmet sağlayıcı ticari unvan, MERSİS/vergi no, adres, KEP/iletişim, ticaret sicil bilgisi, mesleki kuruluş ve yetkili otorite bilgisi vb. bilgileri kolay erişilir şekilde sunmalı (6563 m.3). Madde 3 ayrıntısı ve Yönetmelik madde numaraları bu araştırmada okunamadı.
- Kaynak: https://www.lexpera.com.tr/mevzuat/yonetmelikler/elektronik-ticaret-araci-hizmet-saglayici-ve-elektronik-ticaret-hizmet-saglayicilar-hakkinda-1 ; Yönetmelik RG 29.12.2022 (alomaliye: https://www.alomaliye.com/2022/12/29/elektronik-ticaret-araci-hizmet-saglayici-ve-elektronik-ticaret-hizmet-saglayicilari/)
- Kaynak türü: ikincil
- Doğrulama: kısmen (bilgi listesi genel bilgiye dayanıyor, madde metni görülmedi)

### 3.2 ETBİS kayıt eşikleri (2024/2025/2026 tutarları)
- Kural: ETBİS kaydı için ciro/hacim eşiği yok. Tebliğe göre hizmet sağlayıcılar ve aracı hizmet sağlayıcılar faaliyete başlamadan önce ETBİS'e kayıt olur; değişiklikler 30 gün içinde bildirilir; sınır ötesi e-ticarette ülke/ödeme yöntemi bazında yıllık hacim bildirilir. Yalnızca üçüncü taraf pazaryerinde satanlar için yükümlülük faaliyet modeline göre değişebilir (ikincil). Parasal eşikler ETBİS için değil; 6563'te aracı hizmet sağlayıcı/hizmet sağlayıcı ölçek ve lisans yükümlülükleri içindir: net işlem hacmi 10 milyar TL (orta ölçek; hizmet sağlayıcıda ayrıca 10 milyon işlem), 30 milyar TL ve 60 milyar TL (100 bin işlem) kademeleri yasa/yönetmelik düzeyinde, bu tutarlar yıllık güncelleniyor. 2024, 2025 ve 2026 güncel tutarlar bulunamadı. Küçük bir uygulama geliştiricisi için bu eşikler uygulanabilir değil.
- Kaynak: https://ticaret.gov.tr/duyurular/elektronik-ticaret-bilgi-sistemine-etbis-kayit-ve-bildirim-esaslari (birincil); https://www.erdem-erdem.av.tr/bilgi-bankasi/6563-sayili-elektronik-ticaretin-duzenlenmesi-hakkinda-kanun-kapsaminda-parasal-esiklerin-guncellenmesine-iliskin-duyuru (ikincil)
- Kaynak türü: birincil (ETBİS esasları) + ikincil (parasal eşik haberi)
- Doğrulama: ETBİS "eşik yok": doğrulandı; 2024-2026 parasal eşik tutarları: doğrulanamadı

### 3.3 Ticari elektronik ileti ve İYS
- Kural: Ticari elektronik ileti alıcı onayı (ön izin) gerektirir; alıcı her zaman ret hakkını kullanabilir; tacir/esnaf alıcılar için ön onay şartı yok ama ret hakkı geçerli. Onaylar İYS üzerinden veya yazılı/elektronik alınabilir; İYS kaydı hizmet sağlayıcının kendisince yapılır (e-Devlet veya e-imza), marka tescil belgesi veya yetkilendirme istenir. Onay/ret süreleri için kaynaklarda tutarsız bilgi var (örn. "3 iş günü"), kesin süre doğrulanamadı. Mevcut müşteri ilişkili ürün/servis bildirimi istisnası bir kaynakta var; kapsamı teyit gerekir.
- Kaynak: https://www.iys.org.tr (birincil, içerik okunamadı); https://www.parasut.com/blog/ileti-yonetim-sistemi-hakkinda-bilmeniz-gerekenler ; https://birfatura.com/ileti-yonetim-sistemi-nedir-iys-nedir/
- Kaynak türü: ikincil
- Doğrulama: kısmen

### 3.4 İYS ile KVKK rıza ilişkisi
- Kural: İYS onayı ticari ileti izni içindir; KVKK kapsamındaki kişisel veri işleme şartlarını otomatik karşılamaz. Pazarlama amaçlı veri işlemede ayrıca aydınlatma ve uygun hukuki sebep gerekir. 2026'da bu ilişkiyi değiştiren resmi bir düzenleme bulunamadı.
- Kaynak: https://mailsoftly.com/tr/blog/kvkk-uyumlu-e-posta-pazarlama/ ; https://braverytechnology.com/tr/kvkk-email-pazarlama/
- Kaynak türü: ikincil
- Doğrulama: kısmen

### 3.5 2026 idari para cezaları (6563 m.12)
- Kural: 25.12.2025 RG (33118) tebliği ile 1.1.2026-31.12.2026 için %25,49 yeniden değerleme oranıyla güncellendi. Özet tutarlar (TL): sözleşme öncesi bilgilendirme/sipariş onayı/onaysız ticari ileti 2.859 - 14.309; sipariş teyidi, veri hatası düzeltme, ileti içerik/gönderici bilgisi 2.859 - 28.620; promosyon şartları ve ret yükümlülüğü 5.723 - 42.930; ETBİS bildirim/belge sunmama 143.102 - 715.516; aracı hizmet sağlayıcının tek taraflı sözleşme değişikliği/ekonomik davranışı bozan uygulamalar 28.620 - 286.206. Lisans almama/yenilememe için bir haberde 28.620.688 TL geçiyor; bu tutar özet tablodan teyit edilemedi. Not: Tüketicinin Korunması Kanunu m.77 cezaları ayrı rejimdir ve bu belgede tutarları araştırılmadı. Ticari elektronik ileti cezaları için ayrıca 6563 m.12 değil ilgili madde numarasını doğrulayın.
- Kaynak: https://www.erdem-erdem.av.tr/bilgi-bankasi/elektronik-ticaret-kanunu-kapsaminda-idari-para-cezalari-2026-yili-icin-guncellendi ; https://www.alomaliye.com/2025/12/25/2026-yili-elektronik-ticaretin-duzenlenmesi-hakkinda-kanunun-12-nci-maddesi-ipc/
- Kaynak türü: ikincil (RG tebliği künyesi birden çok kaynakta tutarlı)
- Doğrulama: kısmen (künye ve oran tutarlı; tutarlar tek hukuk bürosu özetinden)

---

## 4) e-Fatura / e-Arşiv (509 sıra no.lu VUK GT)

- Kural: 509 sıra no.lu tebliğe göre genel eşik 2025 hesap dönemi brüt satış hasılatı 3.000.000 TL; e-ticaret faaliyeti olanlar ile gayrimenkul/motorlu taşıt alım-satım-kiralama yapanlar için 500.000 TL; geçiş tarihi 1 Temmuz 2026 olarak aktarılıyor. 31.12.2025 RG'de 589 sıra no.lu VUK GT ile e-arşiv bölümü (IV.2.4.3) değişti; basit usul/işletme hesabı esaslı defter tutanlar için e-arşiv geçişi 2027'ye ertelendi; bilanço esaslılar için kağıt fatura bir kaynağa göre 2026 sonuna kadar sınırlı kullanılabiliyor ve 1 Ocak 2027'de tam e-arşiv başlıyor. 588 sıra no.lu tebliğle 2026 fatura düzenleme sınırı 12.000 TL iddiası ve "parasal sınır kalktı" iddiası çelişkili; doğrulanamadı. Pratik not: e-ticaret yapan mükellefin 500.000 TL eşiği tek başına veya erken geçiş için kritik, bu yüzden mali müşavire eşik/dönem kontrolü yaptırın. 2027 planının ayrıntısı resmi metinden okunamadı.
- Kaynak: https://www.resmigazete.gov.tr/eskiler/2025/12/20251231M5-32.pdf (birincil, PDF metni okunamadı); https://www.ideasoft.com.tr/e-ticaret-icin-e-fatura-zorunlulugu/ ; https://sovos.com/tr/blog/kdv/2025te-e-arsiv-ve-e-fatura-zorunlulugu-nasil-degisti/ ; https://www.turmob.org.tr/arsiv/mbs/resmigazete/-e-Arsiv_Fatura_Duyurusu.pdf
- Kaynak türü: birincil (RG PDF, okunamadı) + ikincil (blog/danışman)
- Doğrulama: kısmen (3 milyon/500 bin ve 1 Temmuz 2026 tutarlı; 589/588 içerikleri ve 2027 planı doğrulanamadı)

---

## 5) Ödeme

### 5.1 Yetkili otorite
- Kural: 6493 sayılı Kanun (20.6.2013) kapsamında ödeme hizmetleri düzenleme ve denetimi TCMB sayfasında yürürlükteki ikincil mevzuatla birlikte listeleniyor (Ödeme Hizmetleri ve E-Para İhracı Yönetmeliği, Bilgi Sistemleri/Veri Paylaşım Tebliği, kripto varlık yasağı yönetmeliği vb.); TCMB faaliyet izinleri veriyor. BDDK'dan TCMB'ye yetki devri 7192 sayılı Kanunla yapıldı (bu bilgi sayfada açık yazmıyor; kendi bilgim ve ikincil kaynaklara dayanıyor). Banka ve kart tarafı için BDDK banka mevzuatı ayrı geçerli.
- Kaynak: https://www.tcmb.gov.tr/wps/wcm/connect/TR/TCMB%20TR/Main%20Menu/Temel%20Faaliyetler/Odeme%20Hizmetleri ; https://www.alomaliye.com/2019/11/22/7192-sayili-kanun-odeme-ve-menkul-kiymet/amp/
- Kaynak türü: birincil (TCMB) + ikincil (alomaliye)
- Doğrulama: kısmen (TCMB rolü teyit edildi, "devir" ifadesi ikincil)

### 5.2 Kart verisi saklama, hosted form, PCI DSS v4.0
- Kural: PCI DSS'e göre CVV/CVC yetkilendirme sonrası saklanamaz; PAN saklanacaksa şifreli/maskeli ve yalnızca gerekirse tutulur. Türkiye'de bankaların üye işyeri kılavuzlarında 6493 ve kart kuruluşu kurallarına uyum, veri güvenliği bölümü bulunuyor. Türk mevzuatında PAN saklama yasağı veren tek bir madde bu araştırmada bulunamadı (TCMB Bilgi Sistemleri Tebliği ve banka kartları yönetmeliği kontrol edilmeli). Pratik: kart verisini kendi sunucunuza hiç almayın; PSP'nin barındırdığı ödeme formu (hosted/iframe/redirect) veya tokenizasyon kullanın, böylece PCI DSS kapsamı SAQ A/A-EP seviyesine iner. PCI DSS v4.0 etkisi (v4.0.1 ile 31 Mart 2025'te zorunlu hale gelen gelecek tarihli gereksinimler, e-ticaret sayfalarında script/iframe bütünlüğü ve ödeme sayfası script yönetimi) kendi bilgimdir, bu araştırmada kaynakla doğrulanmadı.
- Kaynak: https://www-1.ingbank.com.tr/F/Documents/pdf/Bilgi_Destek/Kartli_Odeme_Sistemleri_Kurallari_Uye_Isyeri_Kilavuzu_2022.pdf ; https://www.isbank.com.tr/blog/cvv-kodu-nedir-ne-ise-yarar ; https://www.akbank.com/kurumsal/uye-isyeri-pos/sanal-pos-ozellikleri/kart-saklama
- Kaynak türü: ikincil (banka kılavuz/blog, PCI SSC birincil kaynağı aranmadı)
- Doğrulama: kısmen (CVV yasağı tutarlı; Türk mevzuatında PAN yasağı ve v4.0 detayları doğrulanamadı)

### 5.3 Yerel PSP pratik notu
- Kural: Yerel PSP/sanal POS seçerken lisans (TCMB izinli ödeme kuruluşu veya banka) kontrol edilmeli; 3D Secure uygulaması ve hosted ödeme sayfası/tokenizasyon desteği sorulmalı; kart saklama gerekiyorsa PSP'nin PCI DSS uyumlu kart saklama (tokenization) servisi kullanılmalı. Bu madde pratik öneridir, mevzuat alıntısı değildir.
- Kaynak: https://www.akbank.com/kurumsal/uye-isyeri-pos/sanal-pos-ozellikleri/kart-saklama
- Kaynak türü: ikincil
- Doğrulama: kısmen

---

## 6) DST, GİB özelgesi, mobil uygulama KDV/stopaj

### 6.1 DST oranı 2026
- Kural: 10767 sayılı Cumhurbaşkanı Kararı (karar 24.12.2025, RG 25.12.2025/33118) ile 7194 sayılı Kanun'daki DST oranı %7,5'ten 1.1.2026'dan itibaren %5, 1.1.2027'den itibaren %2,5'e indirildi; yeni oran, yayım sonrası yılbaşından itibaren elde edilen hasılata uygulanır. DST yükümlüsü eşikleri aşan dijital hizmet sağlayıcılardır (küçük geliştirici için genelde ilgisiz; Kanun eşikleri 20 milyon Euro küresel ve 500 milyon TL Türkiye hasılatı, bu tutarlar bu araştırmada doğrulanmadı).
- Kaynak: https://www.alomaliye.com/2025/12/25/dijital-hizmet-vergisi-orani-dusuruldu-2026-yilinda-yuzde-5-2027-yilinda-yuzde-2-5/ ; https://kpmgvergi.com/yayinlar/mali-bultenler/vergi/10767-sayili-cumhurbaskani-karari-ile-7-5-olarak-uygulanan-dijital-hizmet-vergisi-orani-2026-da-5-2027-de-ise-2-5-olarak-uygulanmak-uzere-degistirildi/3344
- Kaynak türü: ikincil (alomaliye, KPMG Vergi); RG künyesi birden çok kaynakta tutarlı
- Doğrulama: doğrulandı (oran ve künye); eşik tutarları doğrulanamadı

### 6.2 GİB özelgesi 30.01.2026
- Kural: İstanbul Defterdarlığı özelgesi, sayı 62030549-125-143061, 30.01.2026; konu Google Play/App Store üzerinden yapay zeka ve mobil oyun uygulaması satışları. Sonuç özeti: uygulamalar yalnızca yurt dışındaki müşteriler tarafından kullanılıyorsa hizmet ihracı sayılır ve KDV hesaplanmaz; yurt içinde de kullanılıyorsa "münhasıran yurt dışı" şartı sağlanmadığı için ihracat istisnası uygulanmaz, genel KDV hükümleri geçerlidir. Kurumlar vergisinde KVK 10/ğ (%80 indirim) ve 32/7 (5 puan) indirimleri yurt içi kullanım varsa uygulanamaz. Özelgede stopaj konusu yok. Özelge yalnızca başvuru sahibini bağlar. Aynı haber sitesinin SSS bölümü özelgeyle uyumsuz (genel KDV istisnası iddiası), bu kısım güvenilmez.
- Kaynak: https://www.alomaliye.com/2026/02/18/app-store-ve-google-playden-elde-edilen-gelirler-nasil-vergilendirilir/ (özelge aslı GİB sitesinde, okunamadı)
- Kaynak türü: ikincil
- Doğrulama: kısmen (özelge künyesi ve sonuç tek ikincil kaynaktan)

### 6.3 Mobil uygulama gelirleri için KDV/stopaj pratik özeti
- Kural: Yurt içi tüketiciye mağaza üzerinden yapılan satışta genel KDV (güncel genel oran %20; bir blogdaki %18 eski) ve gelir/kurumlar vergisi söz konusu. Apple/Google'ın komisyon faturası için geliştirici, yurt dışı hizmet alımı olarak KDV sorumluluğu (sorumlu sıfatıyla KDV) ve stopaj ihtimalini değerlendirmeli (GVK 94, KVK 15 ve KDV m.9 yorumu; bu kısım kendi bilgim). Yurt dışına yönelik reklam gelirlerinde, bir defterdarlık özelgesinde (ikincil aktarma) stopaj/KDV gerekmeyebileceği belirtiliyor. Mobil uygulama gelirleri Türkiye'de tam mükellefiyet kapsamında beyan edilmeli. Mali müşavirle teyit edilmeli.
- Kaynak: https://www.muhasebenews.com/?p=167255 ; https://www.parasut.com/blog/mobil-uygulama-satislarinin-vergilendirilmesi
- Kaynak türü: ikincil
- Doğrulama: kısmen / doğrulanamadı (stopaj konusu net kaynakla doğrulanamadı)

---

## Özet açık noktalar
- Doğrulanamayan: ETBİS dışı parasal eşiklerin 2024-2026 tutarları, 589/588 tebliğ içerikleri, Abonelik Yönetmeliği ve m.52 madde metinleri, 6563 m.3 bilgi listesi, PAN saklama yasağının Türk mevzuatı dayanağı, PCI DSS v4.0 etkisi, stopaj.
- Sonraki adım: mevzuat.gov.tr ve RG PDF'lerini tarayıcıyla (ham metin) okuyup yukarıdaki "kısmen" maddeleri kapatmak.
