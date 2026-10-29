# Aydınlatma ve açık rıza (Kurul İlke Kararı 2026/347)

Kaynak: RG 24.03.2026/33203, Kurul Kararı 18.02.2026 / 2026/347 — birincil, doğrulandı (2026-10-29).

## Kurallar
1. Aydınlatma, işleme şartı ne olursa olsun (açık rıza dahil) **işlemeye başlamadan önce** yapılır; ilgili kişinin talebine veya onayına bağlı değildir.
2. İşleme **açık rızaya** dayanıyorsa aydınlatma metni ile açık rıza metni **ayrı başlıklarla ayrı metinlerdir**.
3. Aynı sayfada duracaksa alt alta, ayrı başlıkla ve **her biri için ayrı beyan** ile sunulur.
4. İşleme açık rıza dışında bir şarta dayanıyorsa **yalnızca aydınlatma** yapılır; ayrıca açık rıza metni sunulmaz.
5. Aydınlatma için onay/rıza istenmez; yalnızca okunduğuna/bilgi edinildiğine dair geri bildirim alınabilir.
6. Başkasının metni birebir kullanılmaz; kendi faaliyetine uyarlanır.
7. Dil açık, sade; genel/belirsiz/eksik/yanıltıcı ifade yok. (Karar örneği: "Kişisel verileriniz Kanun'un 5 ve 6. maddelerinde belirtilen işleme şartları kapsamında işlenmektedir" cümlesi yetersiz.)
8. Uzun ve karmaşık metin kullanılmaz (11. maddeyi tek tek yazmak yerine "Kanun'un 11. maddesi kapsamındaki haklarınız" denebilir).
9. Aydınlatmada işlenen veri ve kategorileri, amaç ve hukuki sebep açık yazılır.
10. Aydınlatmanın ve rızanın usulüne uygun alındığının **ispatı veri sorumlusundadır** → rıza kaydı tut (bkz. `snippets/consent-log.sql`).
11. Aykırılık m.12/1 kapsamında tedbir eksikliği sayılıp m.18 ile işlem yapılabilir.

## Tik/onay ifadeleri
- Aydınlatma sonunda "okudum ve kabul ediyorum / onaylıyorum / açık rıza veriyorum" → **hata**. İyi: "Okudum ve anladım" (bilgi edinme beyanı).
- Tek tikle hem aydınlatma hem rıza → kötü örnek (karar EK-2).
- Ön işaretli kutu: karar metni bu ifadeyi **açıkça kullanmıyor**; ancak Çerez Rehberi rıza için aktif eylem ister ve rıza kategorilerinin panelde başlangıçta pasif gelmesini önemli sayar. Sonuç: rıza kutusunu **ön işaretli sunma** (yorum, kural cümlesi değil).

## UI kontrol listesi
- [ ] Aydınlatma bağlantısı/metni, veri toplanan formda **görünür**; "kabul" kutusu yok, en fazla "Okudum ve anladım".
- [ ] Rıza gerektiren her amaç (pazarlama, profilleme, 3. kişiye aktarım, özel nitelikli veri…) için **ayrı**, ön işaretsiz seçim ve "vermiyorum" seçeneği.
- [ ] Rıza, hizmetin veya sözleşmenin şartı yapılmamış (kayıt için pazarlama rızası zorunlu değil).
- [ ] Rıza geri alma yolu, vermek kadar kolay.
- [ ] Hukuki sebep yanlış etiketlenmemiş: sözleşme/yasal yükümlülük/meşru menfaat varken "rıza" isteme.
- [ ] Rıza kaydı: kim, ne zaman, hangi metin sürümü, hangi amaç, kanal, IP/UA (gerekli ölçüde), geri alma zamanı.
- [ ] Aydınlatma hazırlanırken: veri kategorileri, amaç, hukuki sebep, aktarılan alıcı grupları, **yurt dışı aktarım varsa açıkça**, toplama yöntemi, saklama süresi, 11. madde hakları, başvuru yolu.
- [ ] Yurt dışı aktarım yapılmıyorsa "yapılmaktadır" izlenimi veren ifade yok (ve tersi).

Şablon: `templates/aydinlatma.md`, `templates/acik-riza.md`. Kod: `snippets/consent-log.sql`.
