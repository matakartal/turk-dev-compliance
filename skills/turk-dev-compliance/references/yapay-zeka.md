# Yapay zekâ ve LLM entegrasyonları

Kaynak: KVKK "Yapay Zekâ Alanında Kişisel Verilerin Korunmasına Dair Tavsiyeler" (Nisan 2025, No:76) — birincil, okundu (D). "Üretken Yapay Zekâ ve Kişisel Verilerin Korunması Rehberi (15 Soruda)" (kvkk.gov.tr/Icerik/8547, 24.11.2025) — sayfa okundu, içerik K. 24.02.2025 tarihli duyuru kvkk.gov.tr'de bulunamadı (X). Tavsiyeler bağlayıcı değildir; 2026'da müstakil bir YZ kanunu yürürlükte değildir.

## Geliştirici/üretici/servis sağlayıcıya tavsiyeler (özet)
- Tasarımda gizlilik (privacy by design); veri kalitesi ve **asgari veri**; modelin doğruluğunu sürekli izle.
- Ayrımcılık/önyargı riskini veri toplamadan itibaren her aşamada azalt.
- Yüksek riskte mahremiyet etki değerlendirmesi; projeye özel uyum programı.
- Bireye **itiraz** hakkı ve yalnızca otomatik işlemeye dayalı etkileyici karara maruz kalmama (insan müdahalesi) tasarımı.
- Daha az müdahaleci alternatif sun; işlemeyi durdurma, silme/yok etme/anonimleştirme imkânı tasarla.
- İlgili kişiyi gerekçe, yöntem ve olası sonuçlar hakkında aydınlat; gerekirse etkili onay mekanizması kur.
- Aynı sonuç anonim veriyle mümkünse anonim yöntemi seç; özel nitelikli veride sıkı tedbir; sorumlu/işleyen statüsünü proje başında belirle.

Kaynaklar: YZ Tavsiyeleri (Nisan 2025, No:76) ve **Üretken Yapay Zekâ ve Kişisel Verilerin Korunması Rehberi (Kasım 2025, No:113)** — künye PDF'ten okundu, içeriği bu skill'de ayrıca incelenmedi [K]; LLM entegrasyonu yapmadan önce rehberi oku. kvkk.gov.tr/SharedFolderServer/CMSFiles/MTY5MjNmNmIwZWY3YTE.pdf

## LLM API'si (OpenAI, Anthropic, Google vb.) kullanan uygulama için kontrol listesi
1. **Kişisel veri gidiyor mu?** Prompt'a kullanıcı adı, e-posta, belge, sohbet, sağlık/biyometrik veri dahilse evet. Gitmiyorsa m.9 doğmaz — mümkünse önce maskele/anonimleştir.
2. **Alıcı yurt dışında ise** olağan akış arızi değildir → standart sözleşme (genelde SS-2: sen sorumlu, sağlayıcı işleyen) + 5 iş günü bildirim, ya da veri gitmeyecek şekilde tasarım. Açık rızaya yaslanma (yurt-disi-aktarim.md).
3. Sağlayıcının veri saklama, **model eğitimi için kullanma**, alt işleyen koşulları; sıfır saklama/kurumsal plan seçeneği.
4. Aydınlatma metnine: YZ ile işleme, amaç, alıcı grubu (sağlayıcı), yurt dışı aktarım.
5. Otomatik karar kullanıcıyı etkiliyorsa itiraz/insan müdahalesi yolu.
6. Çıktıda kişisel veri sızıntısı/halüsinasyonla yanlış kişisel bilgi riski; düzeltme/silme talebi akışı.
7. Prompt/yanıt loglarında PII: log politikası ve saklama süresi.
8. Çalışanların kurumsal veriyi kişisel hesaplarla YZ araçlarına yüklemesi için iç politika.
