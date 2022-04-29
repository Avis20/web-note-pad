# ./backend/src/main.py

from uvicorn import run
from fastapi import FastAPI
from tortoise import Tortoise

from fastapi.middleware.cors import CORSMiddleware

from src.database.register import register_tortoise
from src.database.config import TORTOISE_ORM

# разрешим схемам читать связи между моделями
# зачем?
Tortoise.init_models(["src.database.models"], "models")

from src.routes import users

app = FastAPI()

# cors доступы к сайту
app.add_middleware(
    CORSMiddleware,
    allow_origin_regex=".*",
    allow_credentials=True,
    allow_methods="*",
    allow_headers="*",
)
app.include_router(users.router)

register_tortoise(app, config=TORTOISE_ORM, generate_schemas=False)

@app.get("/")
def root():
    return "hello world"


if __name__ == "__main__":
    run("main:app", host="0.0.0.0", port=5000, reload=True)
