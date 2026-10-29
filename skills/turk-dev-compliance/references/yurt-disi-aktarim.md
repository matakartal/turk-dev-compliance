# Yurt dışına aktarım, SDK'lar ve uzak kaynaklar (font/CDN dahil)

Kaynak: Yurt Dışına Aktarım Rehberi (Ocak 2025, No:48) ve 6698 m.9 (7499 ile değişik, 01.06.2024) — birincil, okundu (2026-10-29).

## Aktarım ne zaman var?
Üç kriter: (1) aktaran bir veri sorumlusu/işleyen, (2) alıcı ayrı bir sorumlu/işleyen ve yurt dışında, (3) aktaran veriyi ileterek veya erişilebilir kılarak gönderiyor.
- Hizmet sağlayıcının **yurt dışındaki bulutunda depolama** ve **yurt dışından uzaktan erişim** (destek, ekranda görüntüleme) kriterler sağlanırsa aktarımdır.
- Veri **doğrudan ilgili kişiden** yurt dışı şirkete gidiyorsa (sen aktarmıyorsun) "aktarım" değildir; ama Kanun'un diğer yükümlülükleri sürer.
- Aktarım yoksa m.9 ek yükümlülüğü doğmaz.

## m.9 sıralaması
1. Yeterlilik kararı varsa → (m.5/6 şartıyla) aktarım.
2. Yoksa **uygun güvence**: Kurul standart sözleşmesi (SS-1 sorumlu→sorumlu, SS-2 sorumlu→işleyen, SS-3 işleyen→işleyen, SS-4 işleyen→sorumlu), BŞK, taahhütname (Kurul izniyle), uluslararası sözleşme niteliğinde olmayan kamu anlaşması (izinle) + ilgili kişinin haklarını kullanabilmesi.
3. O da yoksa **yalnızca arızi** aktarım ve sayılan istisnalar (açık rıza + risk bilgilendirmesi, sözleşme ifası vb.). Olağan, düzenli akış arızi sayılmaz → SaaS/SDK akışları için açık rızaya yaslanma.
- Standart sözleşme **metni değiştirilmez** (yalnız seçimlik/alternatif kısımlar), imzalardan itibaren **5 iş günü** içinde Kurum'a bildirilir (fiziki, KEP veya Bildirim Modülü). Bildirmeyene m.18/1(d) para cezası (2026: 90.308–1.806.177 TL). Yönetmelik RG 10.07.2024/32598.

## Uzak font / CDN / script / embed (Google Fonts vb.)
- **Durum: X** — KVKK'nın Google Fonts veya CDN için kararı/rehber ifadesi **bulunamadı**. Almanya'da Münih Bölge Mahkemesi (2022, GDPR) IP adresinin Google'a gitmesi nedeniyle 100 € tazminat verdi; Türkiye için bağlayıcı değildir.
- Rehberdeki üç kriter çerçevesinde değerlendirme (yorum): ziyaretçinin tarayıcısı doğrudan font/CDN sunucusuna bağlanıyor; sen veriyi iletmiyorsun. Ancak risk-azaltma açısından en basit çözüm **self-host**'tur ve maliyeti düşüktür.
- Öneri: fontu/kütüphaneyi kendi origin'inden servis et (`next/font`, `@fontsource/*`, paketi build'e dahil et, SRI gerekmez). Üçüncü taraf kaynak kalıyorsa aydınlatmada alıcı ve ülkeyi belirt, "aktarım var mı" analizini kaydet.
- Aynı sınıf (audit.py işaretler): Google Maps embed, reCAPTCHA, YouTube/Vimeo embed, Gravatar, sosyal widget'lar, jsDelivr/unpkg/cdnjs, Firebase/Crashlytics/analitik, Sentry, Intercom/Zendesk, LLM API'leri, yurt dışı ödeme sağlayıcıları.

## Karar akışı (SDK/servis eklerken)
1. Bu servis **kişisel veri** (IP, cihaz kimliği, e-posta, kullanım olayı) alıyor mu?
2. Veriyi **sen mi gönderiyorsun** (SDK/API/webhook) yoksa tarayıcı doğrudan mı gidiyor?
3. Alıcı yurt dışında mı / yurt dışına erişim var mı (barındırma, destek)?
4. Alıcı **işleyen** mi (adına işliyor: SS-2) yoksa **sorumlu** mu (kendi amacı: SS-1)?
5. Yeterlilik kararı var mı (güncel liste kvkk.gov.tr'de; bu skill listeyi sabitlemez)? Yoksa SS imzala ve 5 iş günü içinde bildir.
6. Aydınlatmada alıcı grubunu ve yurt dışı aktarımı yaz; VERBİS kayıtlıysa orada da işle.
7. Veriyi azalt: IP kısalt, kullanıcı kimliğini hash'le, PII'yi hiç gönderme.
