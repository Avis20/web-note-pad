# ./backend/src/schemas/users.py
from tortoise.contrib.pydantic import pydantic_model_creator
from src.database.models import Users

# Создаем схему на вход
# pydantic_model_creator - хелпер который создает из модели tortoise, схему pydantic
# UserInSchema - нужна для создания новых пользователей
# exclude_readonly - исключить поля которые readonly т.е. id, Datetime с auto_* и т.п.
UserInSchema = pydantic_model_creator(
    Users, name="UserIn", exclude_readonly=True
)

# UserOutSchema - возвращается из апи
UserOutSchema = pydantic_model_creator(
    Users, name="UserOut", exclude=["password", "created_at", "modified_at"]
)

UserDatabaseSchema = pydantic_model_creator(
    Users, name="User", exclude=["created_at", "modified_at"]
)
