# ./backend/src/main.py

import logging
import sys
from uvicorn import run
from fastapi import FastAPI

from fastapi.middleware.cors import CORSMiddleware

from src.models.database import database
from src.settings import get_settings
from src.routers import users

settings = get_settings()

fmt = logging.Formatter(
    fmt="%(asctime)s - %(name)s:%(lineno)d - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
logger = logging.StreamHandler(sys.stdout)
logger.setLevel(logging.DEBUG)
logger.setFormatter(fmt)

app = FastAPI()


@app.on_event("startup")
async def startup():
    # когда приложение запускается устанавливаем соединение с БД
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    # когда приложение останавливается разрываем соединение с БД
    await database.disconnect()


# cors доступы к сайту
app.add_middleware(
    CORSMiddleware,
    allow_origin_regex=".*",
    allow_credentials=True,
    allow_methods="*",
    allow_headers="*",
)
app.include_router(users.router)


@app.get("/")
def root():
    return "hello world"


if __name__ == "__main__":
    run("main:app", host="0.0.0.0", port=5000, reload=True)
