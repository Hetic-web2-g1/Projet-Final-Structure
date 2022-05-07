from sqlalchemy import Table, Column, Integer, String, DateTime, JSON, ARRAY
from datetime import datetime

from src.database.db_engine import metadata

field_table = Table(
    "field",
    metadata,
    Column('id', Integer, primary_key=True),
    Column('id_user', Integer),
    Column('name', String()),
    Column('description', String()),
    Column('location', ARRAY(Integer, dimensions=1)),
    Column('data', JSON),
    Column('img_path', String()),
    Column("created_at", DateTime(), default=datetime.utcnow),
    Column("edited_at", DateTime(), default=datetime.utcnow)
)
