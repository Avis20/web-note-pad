# ./backend/src/database/config.py

import os

TORTOISE_ORM = {
    # Берем из переменной окружения коннект к БД
    "connections": {"default": os.environ.get("DATABASE_URL")},
    "apps": {
        "models": {
            "models": [
                "src.database.models", "aerich.models"
            ],
            "default_connection": "default"
        }
    }
}
