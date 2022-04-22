from sqlalchemy import Table, Column, Integer, String, DateTime, Boolean, ARRAY
from datetime import datetime
from src.database.db_engine import metadata

def create_user():
    user = Table(
            "user",
            metadata,
            Column('id', Integer, primary_key=True),
            Column('is_admin', Boolean),   
            Column('pseudo', String(255)),
            Column('password', String(255)),
            Column('email', String(255)),
            Column('description', String(255)),
            Column('sport_level', Integer),
            Column('favorite', ARRAY(String(255), dimensions=1)),
            Column('date_of_birth', DateTime()),
            Column('location', ARRAY(Integer, dimensions=1)),
            Column('img_path', String(255)),
            Column("created_at", DateTime(), default=datetime.utcnow),
            Column("edited_at", DateTime(), default=datetime.utcnow)
        )

def create_current_user():
    current_user = Table(
        "current_user",
        metadata,
        Column('id', Integer, primary_key=True),
        Column('current_user', ARRAY(Integer(), dimensions=1)),
    )

def create_subscribed_user():
    subscribed_user = Table(
        "subscribed_user",
        metadata,
        Column('id', Integer, primary_key=True),
        Column('subscribed_user', ARRAY(Integer(), dimensions=1)),    
    )