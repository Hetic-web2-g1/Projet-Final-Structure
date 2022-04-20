from sqlalchemy import create_engine, MetaData
from sqlalchemy.exc import SQLAlchemyError
from ..utils.env import db_name, db_pswd, db_type, db_url, db_user

db_info = f"{db_type}://{db_user}:{db_pswd}@{db_url}/{db_name}"
print(db_info)
engine = create_engine(
    db_info,
    pool_size=10,
    max_overflow=0,
)
try:
    engine.connect()
    print("Success")
except SQLAlchemyError as err:
    print("Error", err.__cause__)

# metadata = MetaData()

# metadata.create_all(bind=engine)