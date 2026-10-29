# Ödeme, fatura ve vergi (geliştirici perspektifi)

Çoğu madde ikincil kaynaktan (K); **mali müşavir teyidi şart**. Bu dosya vergi/finans danışmanlığı değildir.

## Kart verisi
- CVV/CVC yetkilendirme sonrası **hiçbir koşulda saklanmaz** (PCI DSS; kaynaklar tutarlı).
- Türk mevzuatında PAN saklamaya dair tek bir madde bulunamadı (X); TCMB Bilgi Sistemleri Tebliği ve banka/kart kuruluşu kuralları kontrol edilmeli.
- Pratik kural: **kartı kendi sunucuna alma.** PSP'nin barındırdığı ödeme sayfası/iframe/redirect veya tokenizasyon kullan → PCI DSS kapsamı küçülür. Kart saklama gerekiyorsa PSP'nin PCI DSS uyumlu token servisi.
- PSP seçerken: TCMB izinli ödeme kuruluşu / banka olup olmadığı, 3D Secure, hosted form, token desteği.
- Düzenleyici: ödeme hizmetleri ve elektronik para (6493) TCMB tarafından düzenlenir ve denetlenir (K). Ödeme toplayan bir platform kuruyorsan lisans konusunda avukata git; PSP'ye bağlanan basit satış bunu gerektirmez (yorum).

## e-Fatura / e-Arşiv (K)
- İkincil kaynaklarda tutarlı: genel eşik 2025 brüt satış hasılatı **3.000.000 TL**; e-ticaret yapanlar için **500.000 TL**; geçiş **01.07.2026**. 589 sıra no.lu VUK GT (31.12.2025) basit usul/işletme hesabı esaslı mükelleflerde e-arşiv geçişini 2027'ye erteliyor; ayrıntı ve 588 sıra no.lu tebliğdeki tutarlar çelişkili (X). 
- Özel entegratör ile e-fatura mükellefi olmadan da e-arşiv düzenlenebilir.
- Sonuç: kendi satışını yapan geliştirici mali müşavirle bu eşiklere bakmalı; sipariş sistemine fatura entegrasyonu (özel entegratör API) planlanmalı.

## Mağaza gelirleri ve vergi (K)
- Dijital Hizmet Vergisi (DST): 10767 sayılı Karar (RG 25.12.2025/33118) → 2026'da **%5**, 2027'de **%2,5** (D). DST yükümlüsü büyük dijital hizmet sağlayıcılardır; küçük geliştirici için genelde ilgisizdir (eşik tutarları doğrulanamadı). Apple'ın Türkiye geliştirici kesintisini güncelleyip güncellemediği doğrulanamadı.
- GİB özelgesi 30.01.2026 (sayı 62030549-125-143061, yalnız başvuru sahibini bağlar): uygulamalar **yalnızca yurt dışındaki** müşterilerce kullanılıyorsa hizmet ihracı/KDV istisnası; yurt içinde de kullanılıyorsa istisna yok, genel KDV ve kurumlar vergisi indirimleri uygulanmaz (K).
- Apple/Google'dan alınan komisyon faturası için sorumlu sıfatıyla KDV/stopaj meselesi ve KDV oranı (%20) için mali müşavire danış.

## Skill çıktısı
Checkout incelemesinde: kart alanı kendi formunda mı (kırmızı bayrak), CVV/PAN loglanıyor mu (`audit.py` `log-pii`), fatura entegrasyonu var mı sorularını sor. Vergi ve fatura kararını **asla** kesin hüküm olarak verme.
