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
ENV PYTHONPATH=$PWD/src

COPY ./src /src

CMD ["poetry", "run", "python", "src/main.py"]
