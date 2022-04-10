# ./backend/Dockerfile

# Базовый образ = python3.10-buster
FROM python:3.10-slim

# Создаем рабочую диру под backend
WORKDIR /app

# уст. переменную окружения PYTHONUNBUFFERED чтобы логи fastapi не застревали в контейнере
ENV PYTHONUNBUFFERED 1

# копируем и уст. зависимости 
ADD pyproject.toml .
RUN pip install poetry
RUN poetry install

COPY ./src .

ENTRYPOINT ["poetry", "run", "python", "main.py"]
