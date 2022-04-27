-- upgrade --
ALTER TABLE "notes" ADD "test" VARCHAR(50);
-- downgrade --
ALTER TABLE "notes" DROP COLUMN "test";
