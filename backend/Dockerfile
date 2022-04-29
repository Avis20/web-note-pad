# ./backend/Dockerfile

# Базовый образ = python3.10-buster
FROM python:3.10-slim

# Создаем рабочую диру под backend
WORKDIR /app

# копируем и уст. зависимости 
ADD pyproject.toml .
RUN pip install poetry
RUN poetry install

# уст. переменную окружения PYTHONUNBUFFERED чтобы логи fastapi не застревали в контейнере
ENV PYTHONUNBUFFERED 1
# Указываем путь до python модулей -> текущая директория, иначе будет ошибка
# backend_1   | ModuleNotFoundError: No module named 'src'
ENV PYTHONPATH=.

# не создавать .pyc файлы в контейнере
ENV PYTHONDONTWRITEBYTECODE 1

COPY ./src /src
COPY migrations ./migrations

CMD ["poetry", "run", "python", "src/main.py"]
