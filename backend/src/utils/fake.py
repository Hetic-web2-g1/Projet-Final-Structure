from datetime import datetime
from faker import Faker
from random import randint

from database.db_engine import engine
from schema.user import UserCreate
from schema.field import FieldCreate
from schema.event import EventCreate
from schema.message import MessageCreate
from manager.UserManager import create_user
from manager.FieldManager import create_field

fake = Faker(locale="fr_FR")

def coordinate():
    lat = 48.8737
    long = 2.2950
    coordinate = []
    coordinate.append((lat * 10000 + randint(0, 50)) / 10000)
    coordinate.append((long * 10000 + randint(0, 50)) / 10000)
    # coordinate.append((lat * 10000 - randint(0, 50)) / 10000)
    # coordinate.append((long * 10000 - randint(0, 50)) / 10000)
    return coordinate

def create_fake_user():
    with engine.begin() as conn:
        user = UserCreate(**{
            'is_admin': fake.boolean(),
            'pseudo': fake.unique.first_name(),
            'password': fake.password(),
            'email': fake.unique.email(),
            'description': fake.text(),
            'sport_level': fake.random_digit(),
            'favorite': [fake.first_name(), fake.first_name()],
            'date_of_birth': datetime.now(),
            'location': coordinate(),
            'img_path': fake.file_path(depth=5, category='image')
        })
        create_user(conn, user)

def create_fake_field():
    with engine.begin() as conn:
        field = FieldCreate(**{
            'id_user': '847acc1f-5862-4f3a-9607-69a86b32f83f',
            'name': fake.unique.first_name(),
            'description': fake.text(),
            'location': coordinate(),
            'img_path': fake.file_path(depth=5, category='image')
        })
        create_field(conn, field)

def create_fake_event():
    pass

def create_fake_message():
    pass

def create_fake_data():
    for _ in range(10):
        create_fake_user()
        create_fake_field()