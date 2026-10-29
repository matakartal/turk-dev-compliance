# App Store ve Google Play gereklilikleri

Kaynak: Apple App Review Guidelines ve App Privacy Details; Google Play Console Yardım (birincil, okundu 2026-10-29). Bunlar kanun değil, mağaza politikalarıdır; sık değişir.

## Apple
- **5.1.1(v) hesap silme:** Hesap oluşturmayı destekleyen uygulama, silmeyi **uygulama içinden** başlatma imkânı sunmalı; gereksiz kişisel veri istenemez; sosyal giriş kullanılıyorsa token iptali.
- **5.1.1(i) gizlilik politikası:** App Store Connect metadatasında ve uygulama içinde; toplanan veri, kullanım, üçüncü taraflar, saklama/silme, rıza geri çekme.
- **App Privacy etiketi:** Her yeni uygulama/sürümde veri türleri, amaç, kullanıcıya bağlılık, tracking; **SDK'ların topladığı veriler dahil**. Privacy Policy URL zorunlu.
- **Çocuk (5.1.4, 1.3):** Kids kategorisinde üçüncü taraf analitik/reklam kısıtlı; ebeveyn kapısı veli rızası yerine geçmez.
- **3.1.1 / 3.1.2:** Dijital içerik/özellik IAP ile; abonelik en az 7 gün, satın almadan önce fiyat ve süre net; loot box oranları önceden. 
- Türkiye'ye özgü yaş şartı veya DST kesintisi duyurusu **doğrulanamadı**; TR fiyat/KDV güncellemeleri Apple Developer News'te (30.10.2025, 10.07.2023).

## Google Play
- **Data safety formu:** Dahili test hariç tüm uygulamalar için zorunlu (veri toplamasan bile); gizlilik politikası bağlantısı zorunlu; SDK verileri dahil, doğru ve güncel.
- **Hesap silme:** Hesap oluşturma sunan uygulamada **uygulama içi silme yolu + kurulum gerektirmeyen web silme linki**; link Data safety'ye girilir.
- **User Data politikası:** Gizlilik politikası Play Console'da ve uygulama içinde; öne çıkan açıklama ve rıza (prominent disclosure); çocuklara yönelik uygulamada Families politikası ve onaylı SDK'lar.
- Türkiye'ye özgü ayrı Play şartı bulunamadı. Play Age Signals API 2026 sonuna kadar küresel yayılıyor (ikincil, opsiyonel).

## Ortak geliştirici listesi
- [ ] Uygulama içi hesap silme (kalıcı silme + yasal saklama istisnaları yazılı) ve web silme sayfası
- [ ] Gizlilik politikası URL'i mağazada ve uygulama içinde; KVKK aydınlatması ile tutarlı
- [ ] SDK envanteri → Privacy etiketi/Data safety ile birebir uyumlu (audit.py `izleyici`, `reklam`, `hata-izleme`)
- [ ] Tracking/izleme için ATT veya rıza akışı
- [ ] Abonelik ekranı: fiyat, süre, yenileme, iptal yolu satın almadan önce
- [ ] Çocuk hedef kitlesi: Kids/Families kuralları + KVKK veli rızası (bkz. `cocuk-ve-yas.md`)
