from sqlalchemy import create_engine, MetaData
from sqlalchemy.exc import SQLAlchemyError
# from utils.env import *
from utils.log import *

db_type="postgresql"
db_url="localhost:5432"
db_user="flamingo"
db_pswd="zeremi"
db_name="who_got_next"

def connect():
    db_info = f"{db_type}://{db_user}:{db_pswd}@{db_url}/{db_name}"
    engine = create_engine(
        db_info,
        pool_size=10,
        max_overflow=0,
    )
    try:
        engine.connect()
        return logging.info("DB connection success")
    except SQLAlchemyError as err:
        return logging.error("Error", err.__cause__)        

    # metadata = MetaData()

    # metadata.create_all(bind=engine)