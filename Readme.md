

## Alembic

```bash
cd src/backend
```

up
```bash
withenv ../../.env.local poetry run alembic upgrade head
```

down
```bash
withenv ../../.env.local poetry run alembic downgrade -1
```

new revision
```bash
withenv ../../.env.local poetry run alembic revision --autogenerate -m 'test'
```
