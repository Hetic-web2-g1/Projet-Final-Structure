from typing import Optional
from fastapi import FastAPI
from sqlalchemy import MetaData
import json
from src.database.db_engine import metadata, engine

metadata.create_all(bind=engine)

from src.manager.user_manager import create_user, get_user_by_id

with engine.begin() as conn:
    create_user(conn)
# Launch api
app = FastAPI()


@app.get("/")
def read_root():
    with engine.begin() as conn:
        print = get_user_by_id(conn)
        return json.dumps(print, default=str)



@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}