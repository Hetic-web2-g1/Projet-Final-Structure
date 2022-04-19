from sqlalchemy import create_engine

user = flamingo
password = zeremi
db_url = "postgresql://user:password@localhost:5432/sqlalchemy"

engine = create_engine(
    settings.database_url,
    pool_size=10,
    max_overflow=1,
)

metadata = MetaData()