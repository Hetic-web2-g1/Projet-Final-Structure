from faker import Faker
from random import randint

from database.db_engine import engine
from schema.user import UserCreate
from manager import UserManager

fake = Faker(locale="fr_FR")

lat = 48.8737
long = 2.2950
coordinate = []
coordinate.append((lat * 10000 + randint(0, 50)) / 10000)
coordinate.append((long * 10000 + randint(0, 50)) / 10000)
# coordinate.append((lat * 10000 - randint(0, 50)) / 10000)
# coordinate.append((long * 10000 - randint(0, 50)) / 10000)
coordinate = {48,2,2982}



for _ in range(10):
    with engine.begin() as conn:
        user = UserCreate(**{
            'is_admin': fake.boolean(),
            'pseudo': fake.unique.first_name(),
            'password': fake.password(),
            'email': fake.unique.email(),
            'description': fake.text(),
            'sport_level': fake.random_digit(),
            'favorite': [fake.first_name(), fake.first_name()],
            'date_of_birth': fake.date(),
            'location': coordinate,
            'img_path': fake.file_path(depth=5, category='image')
        })
        UserManager.create_user(conn, user)