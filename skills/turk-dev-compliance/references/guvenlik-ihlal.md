# Veri güvenliği, ihlal bildirimi ve log saklama

## Veri ihlali (6698 m.12/5, Kurul Kararı 24.01.2019 / 2019/10) — D
- İşlenen verilerin hukuka aykırı elde edilmesi halinde sorumlu **en kısa sürede** ilgili kişiye ve Kurula bildirir; Kurul "en kısa süre"yi **72 saat** olarak yorumlar, süre sorumlunun **öğrenmesinden** başlar.
- 72 saati haklı gerekçeyle aşarsan gecikme gerekçesini yaz; bilgi eksikse aşamalı bildirim yapılabilir.
- Bildirim: "Kişisel Veri İhlal Bildirim Formu" — ihlalbildirim.kvkk.gov.tr. İlgili kişilere makul sürede doğrudan veya sitede ilan.
- **İşleyen** ihlali gecikmeksizin sorumluya bildirir. İhlalin detayları, etkileri, alınan önlemler **kayıt altına alınır**. Olay müdahale planı hazırla.
- İlgili kişi bildiriminin asgari unsurları 2019/271 kararında (ikincil, K).
- Ceza: m.12 ihlali, m.18/1(b): 2026'da 256.357–17.092.242 TL.
- Şablon: `templates/ihlal-bildirimi.md` (runbook + form alanları).

## Geliştirici teknik tedbirleri (öneri düzeyi)
- Aktarımda TLS, bekleyen veride şifreleme, parola için argon2/bcrypt, gizli anahtarlar kod dışında.
- En az yetki, rol bazlı erişim, erişim logları, yedeklerde de silme politikası.
- Log/hata izleme/APM'e **PII göndermeme**: e-posta, telefon, TCKN, kart, token maskele (`snippets/log-masking.ts`).
- Üretim verisini test/staging'e kopyalama; gerekiyorsa anonimleştir.
- Saklama sürelerini koda bağla (TTL/cron), imha kaydı tut (`templates/saklama-imha.md`).
- Üçüncü taraf (işleyen) sözleşmesinde güvenlik ve ihlal bildirim süresi (örn. <24 saat).

## 5651 log saklama ile KVKK minimizasyonu (çelişki yönetimi)
- 5651 Kanun m.5(3): **yer sağlayıcı** trafik bilgisini en az 1, en çok 2 yıl saklar; doğruluk/bütünlük/gizlilik sağlar. Dayanak Yönetmelik (RG 30.11.2007) m.7 hâlâ "6 ay" der → kanunla çelişir (D, K). Pratik: kanundaki alt sınırı baz al, avukata teyit ettir. Erişim sağlayıcı (ISP) için m.6(1)(b) 6 ay–2 yıl.
- Uygulama geliştirici genelde yer sağlayıcıdır **yalnızca kullanıcıların içerik yayımladığı** servislerde (yorum, forum, ilan, sosyal özellik). Salt kurumsal site/SaaS için durum farklı olabilir → avukata sor.
- Bu loglar (IP, zaman, işlem) kişisel veridir: ayrı, erişimi kısıtlı depoda tut, amaç dışı kullanma, süre dolunca sil, imza/zaman damgası ile bütünlük koru. Uygulama logları (debug) ile ayrı tut.
- 7578 ile Siber Güvenlik Başkanlığı atıfları: eski "BTK/Kurum" ifadeleri güncel okunmalı.
