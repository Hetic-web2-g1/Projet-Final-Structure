from sqlalchemy import Table, Column, Integer, String, DateTime
from datetime import datetime
from src.database.db_engine import metadata

def create_message():
    message = Table(
        "message",
        metadata,
        Column('id', Integer, primary_key=True),
        Column('id_user', Integer, nullable=True),
        Column('id_field', Integer, nullable=True),
        Column('id_event', Integer, nullable=True),
        Column('type', String(255)),
        Column('content', String(255)),
        Column("created_at", DateTime(), default=datetime.utcnow),
        Column("edited_at", DateTime(), default=datetime.utcnow)
    )