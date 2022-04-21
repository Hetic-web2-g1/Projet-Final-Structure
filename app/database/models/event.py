from sqlalchemy import Table, Column, Integer, String, DateTime, JSON
from database.db_engine import metadata
from datetime import datetime

def create_event():
    event = Table(
        "event",
        metadata,
        Column('id', Integer, primary_key=True),
        Column('id_user', Integer),
        Column('id_field', Integer),
        Column('name', String(255)),
        Column('description', String(255)),
        Column('data', JSON),
        Column("created_at", DateTime(), default=datetime.utcnow),
        Column("edited_at", DateTime(), default=datetime.utcnow)
    )