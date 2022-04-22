from sqlalchemy import create_engine, MetaData
from sqlalchemy_utils import database_exists, create_database
from sqlalchemy.exc import SQLAlchemyError
from src.utils.log import logging
from src.utils.env import *

# Connection arguments for database
db_info_local = f"{db_type}://{db_user}:{db_pswd}@{db_url}/{db_name}"

# Connextion to database
engine = create_engine(
    db_info_local,
    connect_args={"options": "-c timezone=utc"}
)

# Check existence of db, if not will create it
if not database_exists(engine.url):
    create_database(engine.url)
    logging.info("DB created")

# Try except to test db conncection
try:
    engine.connect()
    logging.info("DB connection success")
except SQLAlchemyError as err:
    engine.connect()
    logging.error("Error", err.__cause__)        

# Creation of metadata
metadata = MetaData()

from src.database.models.user import create_user, create_current_user, create_subscribed_user
from src.database.models.field import create_field
from src.database.models.event import create_event
from src.database.models.message import create_message

# Check existence of tables, if not will create them
if not engine.dialect.has_table(engine.connect(), "user"):
    create_user()
    logging.info("Table user created")
if not engine.dialect.has_table(engine.connect(), "field"):
    create_field()
    logging.info("Table field created")
if not engine.dialect.has_table(engine.connect(), "event"):
    create_event()
    logging.info("Table event created")
if not engine.dialect.has_table(engine.connect(), "message"):
    create_message()
    logging.info("Table message created")
if not engine.dialect.has_table(engine.connect(), "current_user"):
    create_current_user()
    logging.info("Table current_user created")
if not engine.dialect.has_table(engine.connect(), "subscribed_user"):
    create_subscribed_user()
    logging.info("Table subscribed_user created")

# Create all tables stored in metadata
metadata.create_all(bind=engine)