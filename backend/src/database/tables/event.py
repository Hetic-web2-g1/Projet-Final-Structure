from sqlalchemy import Table, Column, Integer, String, DateTime, JSON
from datetime import datetime

from ..db_engine import metadata

event_table = Table(
    "event",
    metadata,
    Column('id', Integer, primary_key=True),
    Column('id_user', Integer),
    Column('id_field', Integer),
    Column('name', String()),
    Column('description', String()),
    Column('data', JSON),
    Column("created_at", DateTime(), default=datetime.utcnow),
    Column("edited_at", DateTime(), default=datetime.utcnow)
)
