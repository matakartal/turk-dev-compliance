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
- Yurt dışı şirket çerezleriyle veri gidiyorsa m.9 + Yönetmelik uygunluğu gerekir (bkz. `yurt-disi-aktarim.md`).

## Geliştirici kuralları
1. Zorunlu olmayan etiketleri (GA/GTM, Meta Pixel, Hotjar, reklam SDK'ları) **rıza verilene kadar yükleme/çalıştırma** (script'i hiç ekleme; yalnızca "anonim mod"a güvenme).
2. `localStorage`/`IndexedDB`'ye kullanıcı kimliği/izleyici yazıyorsan, Rehber kapsam dışı dese de aynı disiplini uygula.
3. Rıza sonucunu 1. taraf çerezde sakla; sürüm numarası tut; metin değişince yeniden sor.
4. Reddet = hiç istek yok (ağ sekmesinde doğrula).

Kod: `snippets/cookie-gate.ts`. Şablon: `templates/cerez-politikasi.md`. Tarama: `scripts/audit.py` (izleyici/GTM/pixel).
