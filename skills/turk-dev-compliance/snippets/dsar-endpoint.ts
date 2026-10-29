// 6698 m.11 başvuruları için minimal uç nokta iskeleti (Express + TypeScript).
// Amaç: başvuruyu kaydet, 30 günlük süreyi izle (m.13), erişim/silme iş akışını tetikle.
// Kimlik doğrulama için mevcut oturumu kullan; fazladan kimlik belgesi isteme.

import express from "express";
const router = express.Router();

type RequestType = "access" | "rectify" | "delete" | "object" | "other";

router.post("/privacy/requests", requireAuth, async (req, res) => {
  const type = req.body.type as RequestType;
  if (!["access", "rectify", "delete", "object", "other"].includes(type)) {
    return res.status(400).json({ error: "invalid_type" });
  }
  const dueAt = new Date(Date.now() + 30 * 24 * 3600 * 1000); // en geç 30 gün
  const id = await db.privacyRequest.create({
    userId: req.user.id,
    type,
    note: String(req.body.note ?? "").slice(0, 2000),
    receivedAt: new Date(),
    dueAt,
    status: "open",
  });
  await notifyPrivacyOwner(id); // sorumluya e-posta/ticket
  res.status(202).json({ id, dueAt });
});

// Erişim: kullanıcının verisini makine okunur dışa aktar
router.get("/privacy/export", requireAuth, async (req, res) => {
  const data = await collectUserData(req.user.id); // tüm tablolar + işleyenlerdeki veriler
  res.setHeader("content-disposition", 'attachment; filename="verilerim.json"');
  res.json(data);
});

// Silme: yasal saklama istisnalarını ayır, gerisini sil / anonimleştir
router.delete("/privacy/account", requireAuth, async (req, res) => {
  await deleteOrAnonymize(req.user.id, {
    retainForLaw: ["invoices"], // örn. fatura: yasal süre dolana kadar kısıtlı tut
  });
  await notifyProcessorsToDelete(req.user.id); // analitik, e-posta servisi, destek aracı vb.
  await auditLog("account_deleted", { userId: req.user.id }); // PII koyma
  res.status(204).end();
});

export default router;

// --- Uygulayıcıya bırakılanlar ---
declare function requireAuth(...a: unknown[]): unknown;
declare const db: any;
declare function notifyPrivacyOwner(id: unknown): Promise<void>;
declare function collectUserData(id: string): Promise<unknown>;
declare function deleteOrAnonymize(id: string, o: { retainForLaw: string[] }): Promise<void>;
declare function notifyProcessorsToDelete(id: string): Promise<void>;
declare function auditLog(e: string, m: Record<string, unknown>): Promise<void>;
