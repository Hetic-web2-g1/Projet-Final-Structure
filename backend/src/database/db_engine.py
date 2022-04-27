from sqlalchemy import create_engine, MetaData
from sqlalchemy_utils import database_exists, create_database
from sqlalchemy.exc import SQLAlchemyError

from src.utils.log import logging
from src.utils.env import settings

# Connection to database
engine = create_engine(
    settings.database_url,
    connect_args={"options": "-c timezone=utc"}
)


# Try except to test db conncection

# A part avoir un success dans les log, ça sert a rien.
# Il y a deja une erreur de sqlalchemy si il n'arrive pas a se co
try:
    engine.connect()
    logging.info("DB connection success")

    # Check existence of db, if not, create it
    if not database_exists(engine.url):
        create_database(engine.url)
        logging.info("DB created")

except SQLAlchemyError as err:
    engine.connect()
    logging.error("Error", err.__cause__)

metadata = MetaData()
