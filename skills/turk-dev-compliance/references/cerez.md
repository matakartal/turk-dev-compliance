# Çerezler ve benzeri teknolojiler

Kaynak: KVKK Çerez Uygulamaları Hakkında Rehber, KVKK Yayını No:69, Temmuz 2025 — birincil, tam metin okundu (2026-10-29). Rehber tavsiye niteliğindedir; bağlayıcı yönetmelik değildir. Rehber **pixel, parmak izi, local storage, beacon** gibi teknolojileri kapsam dışı bırakır (yine de kişisel veri işleniyorsa Kanun uygulanır).

## Sınıflandırma
- **Zorunlu çerez** (rıza gerekmez): Kriter A (iletişimin şebekede sağlanması) veya Kriter B (kullanıcının açıkça istediği hizmet için kesinlikle gerekli): oturum, kimlik doğrulama, güvenlik, kullanıcı seçtiği arayüz tercihi, rıza yönetim çerezi, koşullu birinci taraf analitik. Pazarlama için kullanılamaz. Kalıcı ("beni hatırla") giriş çerezi zorunlu sayılmaz.
- **Zorunlu olmayan** (açık rıza): analitik/performans, reklam/pazarlama, davranışsal reklam (frekans sınırlama, ölçüm dahil), sosyal eklenti takip çerezleri, işlevsellik açıkça istenmediyse işlevsellik çerezleri.

## Rıza kuralları
- Çerez yerleşmeden **önce** rıza; sitede gezinmek rıza değildir; aktif eylem şart.
- Amaç, süre, birinci/üçüncü taraf bilgisi verilir.
- Banner: Kabul / Reddet / Tercihler butonları renk-boyut-punto olarak **eşit görünürlükte** (iyi uygulama).
- Rıza kategorileri yönetim panelinde **başlangıçta pasif**.
- Rıza her zaman geri alınabilir (küçük ikon/şerit ile panele erişim); her ziyarette sorma (rıza yorgunluğu).
- Rıza kullanım sözleşmesine/gizlilik bildirimine iliştirilemez; çerez duvarı rızayı geçersiz kılabilir.
- Üçüncü taraf çerezlerde site sahibi de bilgilendirme ve rıza ile yükümlüdür.
- Yurt dışı şirket çerezleriyle veri gidiyorsa m.9 + Yönetmelik uygunluğu gerekir (bkz. `yurt-disi-aktarim.md`). Rehber bölüm 7.4 (üçüncü taraf: site sahibi + üçüncü taraf birlikte yükümlü) ve bölüm 8 (yurt dışı çerez = m.9) [D].
- Birinci taraf analitikte IP maskeleme veri minimizasyonu örneği olarak önerilir [K]. Rehberde "IP adresi kişisel veridir" veya Google Fonts/CDN'e dair ifade **yoktur** [X].

## Kurul kararı örnekleri (karar özeti, D; tutarlar o yılın rakamıdır)
- 2022/229 (e-ticaret, web+mobil): zorunlu olmayan/yurt dışı 3. taraf çerezler rızasız → 800.000 TL. "Yerel sağlayıcı yok" savunması reddedildi. kvkk.gov.tr/Icerik/7275
- 2023/1645 (oyun dağıtıcısı): yurt dışı 3. taraf çerezleri "gerekli" saymak, "ziyaret = onay" metni → 750.000 TL. kvkk.gov.tr/Icerik/7765
- 2024/1361 (eğitim kurumu sitesi): analitik çerezde opt-in yok → 250.000 TL + aydınlatma 15.000 TL. kvkk.gov.tr/Icerik/8884

## Geliştirici kuralları
1. Zorunlu olmayan etiketleri (GA/GTM, Meta Pixel, Hotjar, reklam SDK'ları) **rıza verilene kadar yükleme/çalıştırma** (script'i hiç ekleme; yalnızca "anonim mod"a güvenme).
2. `localStorage`/`IndexedDB`'ye kullanıcı kimliği/izleyici yazıyorsan, Rehber kapsam dışı dese de aynı disiplini uygula.
3. Rıza sonucunu 1. taraf çerezde sakla; sürüm numarası tut; metin değişince yeniden sor.
4. Reddet = hiç istek yok (ağ sekmesinde doğrula).

Kod: `snippets/cookie-gate.ts`. Şablon: `templates/cerez-politikasi.md`. Tarama: `scripts/audit.py` (izleyici/GTM/pixel).
