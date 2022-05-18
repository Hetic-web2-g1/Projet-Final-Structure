from fastapi import FastAPI

from routers import index, users
from database.db_engine import metadata, engine

from database.tables import user, field, event, message

metadata.create_all(bind=engine)


# Launch api
app = FastAPI()

app.include_router(index.router)
app.include_router(users.router)

from utils.fake import create_fake_data
# create_fake_data()