from fastapi import APIRouter
from typing import List

from src.database.db_engine import engine

router = APIRouter(
    prefix="",
    tags=["Index"],
)

@router.get("/")
def read_root():
    return [{"msg": "Welcome to the Jungle"}]