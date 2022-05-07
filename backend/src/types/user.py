from datetime import datetime
from typing import List
from pydantic import BaseModel


class UserCreate(BaseModel):
    is_admin: bool
    pseudo: str
    password: str
    email: str
    description: str
    sport_level: int
    favorite: List[str]
    date_of_birth: datetime
    location: List[int]
    img_path: str


class User(UserCreate):
    id: int
    created_at: datetime
    edited_at: datetime
