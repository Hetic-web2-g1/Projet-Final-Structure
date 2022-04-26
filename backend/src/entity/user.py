from dataclasses import dataclass
from datetime import datetime
from typing import List

@dataclass
class UserCreate:
    is_admin: bool
    pseudo: str
    password: str
    email: str
    description: str
    sport_level: int
    favorite: List [str]
    date_of_birth: datetime
    location: List[int]
    img_path: str

@dataclass
class User(UserCreate):
    id: int
    created_at: datetime = datetime.utcnow()
    edited_at: datetime = datetime.utcnow()