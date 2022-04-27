from routers.users import users_api
from fastapi import FastAPI

from database.db_engine import metadata, engine

metadata.create_all(bind=engine)


# Launch api
app = FastAPI()

app.include_router(users_api.router)
