# Ödeme, fatura ve vergi (geliştirici perspektifi)

Çoğu madde ikincil kaynaktan (K); **mali müşavir teyidi şart**. Bu dosya vergi/finans danışmanlığı değildir.

## Kart verisi
- CVV/CVC yetkilendirme sonrası **hiçbir koşulda saklanmaz** (PCI DSS; kaynaklar tutarlı).
- PAN için tek başına "saklanamaz" diyen madde yok; ama 5464 sayılı Kanun m.23: üye işyeri kart ve kart hamili bilgilerini hamilin **yazılı rızası olmadan** açıklayamaz, saklayamaz, kopyalayamaz (kasten ihlal m.39: 1–3 yıl hapis + adli para cezası) (D). Banka Kartları ve Kredi Kartları Hakkında Yönetmelik m.27/A(7): üye işyeri ve anlaşmalı kuruluşlar veri işlemede asgari PCI DSS hükümlerini dikkate alır (D; 2013 sonrası değişiklikler taranmadı, K). PCI DSS'in kendisi sözleşmesel standarttır. Pratik: PAN/CVV'yi hiç saklama, hosted form/token kullan.
- Pratik kural: **kartı kendi sunucuna alma.** PSP'nin barındırdığı ödeme sayfası/iframe/redirect veya tokenizasyon kullan → PCI DSS kapsamı küçülür. Kart saklama gerekiyorsa PSP'nin PCI DSS uyumlu token servisi.
- PSP seçerken: TCMB izinli ödeme kuruluşu / banka olup olmadığı, 3D Secure, hosted form, token desteği.
- Düzenleyici: ödeme hizmetleri ve elektronik para (6493) TCMB tarafından düzenlenir ve denetlenir (D: 7192 ile BDDK yetkileri TCMB'ye geçti; 6493 m.3(b); tcmb.gov.tr). Banka/kredi kartı sistemleri 6493 kapsamı dışındadır, 5464'e tabidir (6493 m.24). Ödeme toplayan bir platform kuruyorsan lisans konusunda avukata git; PSP'ye bağlanan basit satış bunu gerektirmez (yorum).

## e-Fatura / e-Arşiv (K)
- VUK Genel Tebliği 509 güncel metni (GİB) IV.1.4(a): e-Fatura zorunluluğu brüt satış hasılatı **3.000.000 TL** ve üzeri; internet ortamında aracı hizmet sağlayıcılar ve kendi sitesinde/elektronik ortamda mal-hizmet satanlar için **500.000 TL**. Geçiş: ilgili hesap dönemini izleyen yılın yedinci ayının başı (2025 dönemi için **01.07.2026**) (D). **589 sıra no.lu tebliğ** (RG 31.12.2025) yalnızca basit usul ve işletme hesabı esaslı mükelleflerin tutara bakılmaksızın e-Arşiv geçişini 01.01.2027'ye erteler; başka tutar içermez. 588 sıra no.lu tebliğ e-fatura değil VUK yeniden değerleme tebliğidir. Hangi gruba girdiğini mali müşavire sor. 
- Özel entegratör ile e-fatura mükellefi olmadan da e-arşiv düzenlenebilir.
- Sonuç: kendi satışını yapan geliştirici mali müşavirle bu eşiklere bakmalı; sipariş sistemine fatura entegrasyonu (özel entegratör API) planlanmalı.

## Mağaza gelirleri ve vergi (K)
- Dijital Hizmet Vergisi (DST): 10767 sayılı Karar (RG 25.12.2025/33118) → 2026'da **%5**, 2027'de **%2,5** (D). DST yükümlüsü büyük dijital hizmet sağlayıcılardır; küçük geliştirici için genelde ilgisizdir (eşik tutarları doğrulanamadı). Apple'ın Türkiye geliştirici kesintisini güncelleyip güncellemediği doğrulanamadı.
- GİB özelgesi 30.01.2026 (sayı 62030549-125-143061, yalnız başvuru sahibini bağlar): uygulamalar **yalnızca yurt dışındaki** müşterilerce kullanılıyorsa hizmet ihracı/KDV istisnası; yurt içinde de kullanılıyorsa istisna yok, genel KDV ve kurumlar vergisi indirimleri uygulanmaz (K).
- Apple/Google'dan alınan komisyon faturası için sorumlu sıfatıyla KDV/stopaj meselesi ve KDV oranı (%20) için mali müşavire danış.

## Skill çıktısı
Checkout incelemesinde: kart alanı kendi formunda mı (kırmızı bayrak), CVV/PAN loglanıyor mu (`audit.py` `log-pii`), fatura entegrasyonu var mı sorularını sor. Vergi ve fatura kararını **asla** kesin hüküm olarak verme.
