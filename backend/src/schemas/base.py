# ./backend/src/schemas/base.py

from pydantic import BaseModel


class Status(BaseModel):
    message: str

class LogginSchema(BaseModel):
    success: int = 1
    message: str = "Loggined"
