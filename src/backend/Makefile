
SHELL = /usr/bin/bash -i

LOCAL_ENV_FILE = ../../.env.local

.PHONY: new_revision
new_revision:
	@withenv $(LOCAL_ENV_FILE) poetry run alembic revision --autogenerate -m "init";

.PHONY: upgrade
upgrade:
	@withenv $(LOCAL_ENV_FILE) poetry run alembic upgrade head;

.PHONY: downgrade
downgrade:
	@withenv $(LOCAL_ENV_FILE) poetry run alembic downgrade -1;

