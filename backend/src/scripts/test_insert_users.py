from sqlalchemy.exc import NoResultFound

from src.models.users import Users
from src.models.database import sync_session

session = sync_session()

user = {
    "username": "test",
    "full_name": "test",
    "password": "test",
}
session.begin()

try:
    db_user = session.query(Users).where(Users.username == user.get("username")).one()
except NoResultFound:
    session.add(Users(**user))

session.commit()
