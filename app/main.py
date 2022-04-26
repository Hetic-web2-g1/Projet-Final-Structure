from typing import Optional
from fastapi import FastAPI
from sqlalchemy import MetaData

from src.database.db_engine import metadata, engine

metadata.create_all(bind=engine)

from src.manager.user_manager import create_user
# conn = engine.connect()
with engine.begin() as conn:
    create_user(conn)

# Launch api
app = FastAPI()


@app.get("/")
def read_root():
    return {"Backend"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}