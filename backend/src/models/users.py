# ./backend/models/users.py

import sqlalchemy as sa
from sqlalchemy import func

metadata = sa.MetaData()


users_table = sa.Table(
    "users",
    metadata,
    sa.Column("id", sa.Integer, primary_key=True),
    sa.Column("username", sa.String(20), unique=True),
    sa.Column("full_name", sa.String(20), nullable=True),
    sa.Column("password", sa.String(128), nullable=True),
    sa.Column("created_at", sa.TIMESTAMP(timezone=False), server_default=func.now()),
    sa.Column("modified_at", sa.TIMESTAMP(timezone=False), server_default=func.now()),
)
