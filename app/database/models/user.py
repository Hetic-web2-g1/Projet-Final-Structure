from lib2to3.pgen2.token import STRING
from sqlite3 import Timestamp
from time import time
from xmlrpc.client import Boolean
from sqlalchemy import Table, Column, Integer, String, Boolean, DateTime, Float, ARRAY
from database.db_engine import metadata
from datetime import datetime
...
# model_object.updated_at = datetime.now(timezone.utc)

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
            Column("latitude", Integer),
            Column("longitude", Integer),
            Column('img_path', String(255)),
            Column("created_at", DateTime(), default=datetime.utcnow),
            Column("edited_at", DateTime(), default=datetime.utcnow)
        )
