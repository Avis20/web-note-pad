# Мини сервис для написания заметок
Стек: backend - fastapi, frontend - vue


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
