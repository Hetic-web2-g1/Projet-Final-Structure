from sqlalchemy import Table, Column, Integer, String, DateTime, JSON, ARRAY
from database.db_engine import metadata
from datetime import datetime

def create_field():
    field = Table(
        "field",
        metadata,
        Column('id', Integer, primary_key=True),
        Column('id_user', Integer),
        Column('name', String(255)),
        Column('description', String(255)),
        Column('location', ARRAY(Integer, dimensions=1)),
        Column('data', JSON),
        Column('img_path', String(255)),
        Column("created_at", DateTime(), default=datetime.utcnow),
        Column("edited_at", DateTime(), default=datetime.utcnow)
    )