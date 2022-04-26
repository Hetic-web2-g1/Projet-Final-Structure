from sqlalchemy import select, insert
from sqlalchemy.engine import Connection
from datetime import datetime

from src.entity.user import User
from src.database.schema.user import user

def get_user_by_id(conn):
    stmt = select([user])

    data = conn.execute(stmt)

    if data is not None:
        data = dict(data)
        return User(**data)

def create_user(conn: Connection):
    stmt = insert(user, values={
        'is_admin' : True,
        'pseudo' : 'Zeremie',
        'password' : 'Zeremie',
        'email' : 'zeremie@zeremie.zeremie',
        'description' : 'zeremie',
        'sport_level' : 999,
        'favorite' : [3],
        'date_of_birth' : datetime.now(),
        'location' : [222, 333],
        'img_path' : 'zeremie/zeremie/zeremie/zeremie.zeremie'
    })

    data = conn.execute(stmt).first()

    if data is not None:
        data = dict(**data)
        print(data)
        return User(**data)