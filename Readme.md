
## From [Developing a Single Page App with FastAPI and Vue.js](https://testdriven.io/blog/developing-a-single-page-app-with-fastapi-and-vuejs/)

* Original rep = [fastapi-vue](https://github.com/testdrivenio/fastapi-vue)


### Создание новой ревизии

```
docker-compose exec backend poetry run alembic revision --autogenerate -m "<название ревизии>"

```

### Запуск в debug режиме

```
export PYTHONPATH=./src
```
