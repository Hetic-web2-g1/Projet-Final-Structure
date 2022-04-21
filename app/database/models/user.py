from time import time
from xmlrpc.client import Boolean
from sqlalchemy import Table, Column, Integer, String
from database.db_engine import metadata

def create_user():
    user = Table(
        "user",
        metadata,
        Column('id', Integer, primary_key=True),
        Column('pseudo', String(30)),
        Column('email', String)
    )

# def create_usersq():
#     user = Table(
#         "user",
#         metadata,
#         Column('id', Integer, primary_key=True),
#         Column('is_admin', Boolean),   
#         Column('pseudo', String(20)),
#         Column('password'),
#         Column('email', String(20)),
#         Column('description'),
#         Column('sport_level'),
#         Column('favorite'),
#         Column('date_of_birth'),
#         Column('location'),
#         Column('img_path'),
#         Column('timestamp'),
#         Column(DateTime(timezone=True),
#         Column(DateTime(timezone=True)
# )
#     )
