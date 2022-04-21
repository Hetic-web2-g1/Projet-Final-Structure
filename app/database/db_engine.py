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

from database.models.user import create_user

if not engine.dialect.has_table(engine.connect(), "user"):
    create_user()


metadata.create_all(bind=engine)
