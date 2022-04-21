from sqlalchemy import create_engine, MetaData
from sqlalchemy_utils import database_exists, create_database
from sqlalchemy.exc import SQLAlchemyError
from utils.env import *
from utils.log import *

db_info_local = f"{db_type}://{db_user}:{db_pswd}@{db_url}/{db_name}"
engine = create_engine(
    db_info_local,
    pool_size=10,
    max_overflow=0,
    connect_args={"options": "-c timezone=utc"}
)

if not database_exists(engine.url):
    create_database(engine.url)

try:
    engine.connect()
    logging.info("DB connection success")
except SQLAlchemyError as err:
    engine.connect()
    logging.error("Error", err.__cause__)        

metadata = MetaData()

from database.models.user import create_user, create_current_user, create_subscribed_user
from database.models.field import create_field
from database.models.event import create_event
from database.models.message import create_message

if not engine.dialect.has_table(engine.connect(), "user"):
    create_user()
if not engine.dialect.has_table(engine.connect(), "current_user"):
    create_current_user()
if not engine.dialect.has_table(engine.connect(), "subscribed_user"):
    create_subscribed_user()
if not engine.dialect.has_table(engine.connect(), "field"):
    create_field()  
if not engine.dialect.has_table(engine.connect(), "event"):
    create_event()
if not engine.dialect.has_table(engine.connect(), "message"):
    create_message()

metadata.create_all(bind=engine)