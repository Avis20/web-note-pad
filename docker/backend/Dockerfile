FROM python:3.11-slim

# Основной путь приложения
ENV SRC_DIR=/opt

# Путь до приложения fastapi
ENV APP_DIR=$SRC_DIR/app

# Установка зависимостей
WORKDIR $SRC_DIR

ENV PATH="/$SRC_DIR/.local/bin:${PATH}"
RUN pip install --upgrade pip && \
    pip install --no-cache-dir poetry

COPY ./src/backend/pyproject.toml pyproject.toml
RUN poetry install --no-root --only main

# Копирования кода приложения
COPY ./src/backend/app $APP_DIR
COPY ./src/backend/alembic.ini $SRC_DIR/alembic.ini
COPY ./src/backend/migrations $SRC_DIR/migrations

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1
