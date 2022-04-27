-- upgrade --
ALTER TABLE "notes" DROP COLUMN "test";
-- downgrade --
ALTER TABLE "notes" ADD "test" VARCHAR(50);
