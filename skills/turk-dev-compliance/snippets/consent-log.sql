-- Rıza kaydı (ispat yükü veri sorumlusunda — Kurul 2026/347). PostgreSQL.
-- Her amaç ayrı satır; geri alma yeni satırla veya revoked_at ile; metin sürümü saklanır.

CREATE TABLE consent_text (
  id          bigserial PRIMARY KEY,
  purpose     text NOT NULL,            -- örn. 'marketing_email'
  version     int  NOT NULL,
  body        text NOT NULL,            -- kullanıcıya gösterilen tam rıza metni
  created_at  timestamptz NOT NULL DEFAULT now(),
  UNIQUE (purpose, version)
);

CREATE TABLE consent_record (
  id               bigserial PRIMARY KEY,
  user_id          uuid NOT NULL,
  purpose          text NOT NULL,
  text_version     int  NOT NULL,
  decision         boolean NOT NULL,    -- true: veriyorum, false: vermiyorum
  given_at         timestamptz NOT NULL DEFAULT now(),
  revoked_at       timestamptz,
  channel          text NOT NULL,       -- 'web' | 'ios' | 'android' | 'api'
  -- ihtiyaç ölçüsünde; IP'yi tam tutmak zorunda değilsin (kısaltılmış/hash yeterli olabilir)
  ip_truncated     inet,
  user_agent       text,
  FOREIGN KEY (purpose, text_version) REFERENCES consent_text (purpose, version)
);

CREATE INDEX ON consent_record (user_id, purpose, given_at DESC);

-- Güncel durum: son kayıt, geri alınmamışsa ve decision = true ise rıza vardır.
CREATE VIEW consent_current AS
SELECT DISTINCT ON (user_id, purpose) user_id, purpose, decision, given_at, revoked_at, text_version
FROM consent_record
ORDER BY user_id, purpose, given_at DESC;
