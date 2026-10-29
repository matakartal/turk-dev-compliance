// Mesafeli Sözleşmeler Yönetmeliği'ne uygun checkout bloğu (React). Metinleri kendi
// faaliyetine göre uyarla; avukat/mali müşavir teyidi al.
// - Fiyat KDV dahil; abonelikte dönem bazında tutar
// - Ön bilgilendirme formu ve sözleşme AYRI onay; kutular ön işaretsiz
// - Ödeme yükümlülüğü ifadesi butonun hemen üstünde
// - Dijital ürünse anında ifa + cayma hakkı kaybı için AYRI onay
// - Ek ücretli seçenek ön seçili değil (m.19/2)
// - Kart girişi kendi alanında değil: PSP'nin hosted/iframe bileşeni

import { useState } from "react";

type Props = {
  priceInclVat: string;       // "249,00 TL"
  billingPeriod?: string;     // "aylık" (abonelik)
  isDigital: boolean;
  onPay: () => void;
  PaymentFrame: React.ComponentType; // PSP hosted fields
};

export function Checkout({ priceInclVat, billingPeriod, isDigital, onPay, PaymentFrame }: Props) {
  const [preInfo, setPreInfo] = useState(false);
  const [contract, setContract] = useState(false);
  const [immediate, setImmediate] = useState(false);
  const ready = preInfo && contract && (!isDigital || immediate);

  return (
    <form onSubmit={(e) => { e.preventDefault(); if (ready) onPay(); }} style={{ fontSize: 16 /* ≥12 punto */ }}>
      <p>
        Toplam (tüm vergiler dahil): <strong>{priceInclVat}</strong>
        {billingPeriod && <> / {billingPeriod}. Her dönem otomatik yenilenir; istediğiniz zaman Ayarlar &gt; Abonelik'ten iptal edebilirsiniz.</>}
      </p>

      <PaymentFrame />

      <label>
        <input type="checkbox" checked={preInfo} onChange={(e) => setPreInfo(e.target.checked)} />{" "}
        <a href="/on-bilgilendirme" target="_blank">Ön Bilgilendirme Formu</a>'nu okudum ve teyit ediyorum.
      </label>
      <label>
        <input type="checkbox" checked={contract} onChange={(e) => setContract(e.target.checked)} />{" "}
        <a href="/mesafeli-satis" target="_blank">Mesafeli Satış Sözleşmesi</a>'ni okudum ve onaylıyorum.
      </label>
      {isDigital && (
        <label>
          <input type="checkbox" checked={immediate} onChange={(e) => setImmediate(e.target.checked)} />{" "}
          Cayma süresi dolmadan hizmetin ifasına başlanmasını talep ediyorum; ifa başladığında cayma hakkımı kaybedeceğimi biliyorum.
        </label>
      )}

      <p><strong>Siparişi onayladığınızda ödeme yapma yükümlülüğü altına girersiniz.</strong></p>
      <button type="submit" disabled={!ready}>Siparişi onayla ve öde</button>
      {/* Pazarlama rızası bu formda ödeme şartı olmamalı; ayrı ve ön işaretsiz sunulur. */}
    </form>
  );
}
