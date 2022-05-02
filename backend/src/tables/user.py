from sqlalchemy import Table, Column, Integer, String, DateTime, Boolean, ARRAY
from datetime import datetime

from src.database.db_engine import metadata

user_table = Table(
    "user",
    metadata,
    Column('id', Integer, primary_key=True),
    Column('is_admin', Boolean),
    Column('pseudo', String()),
    Column('password', String()),
    Column('email', String()),
    Column('description', String()),
    Column('sport_level', Integer),
    Column('favorite', ARRAY(String(), dimensions=1)),
    Column('date_of_birth', DateTime()),
    Column('location', ARRAY(Integer, dimensions=1)),
    Column('img_path', String()),
    Column("created_at", DateTime(), default=datetime.utcnow),
    Column("edited_at", DateTime(), default=datetime.utcnow)
)

current_user_table = Table(
    "current_user",
    metadata,
    Column('id', Integer, primary_key=True),
    Column('current_user', ARRAY(Integer(), dimensions=1)),
)

subscribed_user_table = Table(
    "subscribed_user",
    metadata,
    Column('id', Integer, primary_key=True),
    Column('subscribed_user', ARRAY(Integer(), dimensions=1)),
)
