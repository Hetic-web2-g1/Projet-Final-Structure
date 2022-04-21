from typing import Optional
from fastapi import FastAPI
from database.db_engine import *



from sqlalchemy import text
with engine.connect() as conn:
    result = conn.execute(text("select 'hello world'"))
    print(result.all())

app = FastAPI()


@app.get("/")
def read_root():
    return {"Backend"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}