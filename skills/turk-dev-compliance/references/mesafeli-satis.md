# Satın alma / checkout ekranı gereklilikleri

Kaynak: Mesafeli Sözleşmeler Yönetmeliği (RG 27.11.2014/29188) metni okundu (D); 24.05.2025/32909 değişikliği RG HTML tam metninden okundu (D), yürürlük 01.01.2026: m.5/1 (g) iade için satıcının öngördüğü taşıyıcı bilgisi; (k) hakem heyeti / dava öncesi arabuluculuk bilgisi; m.12/5 satıcının belirttiği taşıyıcıyla iadede masraf tüketiciye yüklenemez, taşıyıcı belirtilmemişse iade masrafı istenemez; m.13/3 ve m.15/1 (i) kaldırıldı. (ğ), (h), (e) bentleri değişmedi. Güncel konsolide metni mevzuat.gov.tr'den kontrol et. Tüketici ile web/uygulama üzerinden sözleşme kuruyorsan geçerli; **App Store/Google Play IAP satışında ön bilgilendirme ve ödemeyi mağaza yürütür** (geliştirici kendi web/3. taraf ödemesinde sorumludur; bu ayrım ikincil yorum).

## Madde bazında
- **m.5 ön bilgilendirme:** temel nitelikler; satıcı kimliği/adres/iletişim; şikâyet kanalı; cayma koşulları ve bildirim adresi; uyuşmazlık mercileri; **tüm vergiler dahil toplam fiyat** (+kargo/ek masraf); dijital içerikte teknik koruma ve uyumlu donanım/yazılım. **Abonelikte** toplam maliyet **her faturalama dönemi bazında**. İspat yükü satıcıda.
- **m.6–7:** en az 12 punto; ödeme yükümlülüğünden **hemen önce** temel bilgiler ayrıca gösterilir; tüketici teyit etmezse sözleşme kurulmuş sayılmaz. Sıra: ön bilgilendirme formu → onay → mesafeli satış sözleşmesi ayrıca onaya sunulur.
- **m.8:** Siparişi onaylamadan hemen önce siparişin **ödeme yükümlülüğü doğurduğu** açıkça bildirilir; yoksa tüketici siparişle bağlı değildir. **Buton adı için sabit ifade zorunluluğu yoktur**; "Siparişi onayla ve öde" gibi net bir ifade iyi uygulamadır, "zorunlu" diye sunma.
- **m.15 cayma istisnaları (özet):** (ğ) elektronik ortamda anında ifa edilen hizmetler / anında teslim edilen gayrimaddi mallar; (e) koruyucu unsuru açılmış dijital içerik; (h) cayma süresi dolmadan tüketici onayıyla ifaya başlanan hizmetler. Genel cayma süresi 14 gün. Dijital ürün/abonelikte **cayma hakkı bilgilendirmesi + anında ifa onayı** ayrı onay olarak alınır (uygulama yorumu; avukat teyidi öner). m.15 bent numaraları değişmiş olabilir (Danıştay iptal notu tek kaynakta, X).
- **m.19(2):** Tüketicinin açık onayı olmadan ek ödeme doğuran seçenekler **önceden seçili** sunulmuşsa ödemeler derhal iade edilir → ön işaretli add-on/sigorta/bağış/yenileme kutusu yok.
- **2025 değişikliği:** iade taşıyıcısı belirtilmişse iade masrafı tüketiciye yüklenemez; taşıyıcı belirtilmemişse iade bedeli talep edilemez; hakem heyeti/arabuluculuk bilgisi (K).
- **Abonelik** — Abonelik Sözleşmeleri Yönetmeliği (RG 24.01.2015/29246, 6502 m.52) metni okundu (D); konsolide yürürlük teyidi alınamadı, mülga/değişiklik kaydı da görülmedi (K). Dijital aboneliklere m.2/2 gereği yalnız m.5, 6, 7, 8, 13, 22–25 uygulanır: **m.13** belirli süreli sözleşmeye "otomatik uzar" hükmü konamaz; uzatma ancak kuruluştan sonra tüketicinin talebi/onayıyla olur; onaysız devam eden hizmet için bedel istenemez. **m.22–25**: belirsiz süreli veya ≥1 yıllık sözleşmede gerekçesiz/cezasız fesih hakkı; fesih sistemi kesintisiz açık ve kuruluş yönteminden ağır olmayan (m.23/3); talep en geç 7 gün içinde yerine getirilir (m.24/1); kalan tutar 15 günde iade (m.25). Ticaret Bakanlığı güncelleme çalışması yürütüyor (Ekim 2026), yeni kural yayımlanmadı. Yorum: otomatik yenilenen aylık abonelikte açık onay ve kolay iptal akışı kur; avukata teyit ettir.

## Checkout kontrol listesi
- [ ] Fiyat KDV dahil, kargo/ek masraf ayrı ve ödeme öncesi görünür
- [ ] Abonelik: dönem başına tutar, süre, yenileme tarihi, iptal yolu, deneme bitişi
- [ ] Ön bilgilendirme formu ve mesafeli satış sözleşmesi ödeme butonundan önce, ≥12 punto, ayrı onayla
- [ ] Onay kutuları **ön işaretsiz**; ek ücretli seçenek ön seçili değil
- [ ] "Ödeme yükümlülüğü doğurur" ifadesi butonda/hemen üstünde
- [ ] Dijital içerikte: anında ifa onayı + cayma hakkı kaybı bilgisi
- [ ] Cayma/iade/iptal bağlantısı ve satıcı kimliği (unvan, MERSİS/VKN, adres, KEP/telefon)
- [ ] Sipariş sonrası: sözleşme + ön bilgilendirme kopyası kalıcı veri saklayıcıda (e-posta/PDF), sipariş onay e-postası
- [ ] Pazarlama rızası ödeme şartı değil, ayrı ve ön işaretsiz
- [ ] Kart verisi sunucuna uğramıyor (bkz. `odeme-vergi.md`)

Şablon: `templates/on-bilgilendirme-formu.md`, `templates/mesafeli-satis-sozlesmesi.md`. Kod: `snippets/checkout.tsx`.
