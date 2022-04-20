from typing import Optional
from fastapi import FastAPI
from database import engine

engine.connect()

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}