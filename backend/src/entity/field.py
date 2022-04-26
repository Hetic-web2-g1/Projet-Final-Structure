from dataclasses import dataclass
from datetime import datetime
from typing import List

@dataclass
class Data:
    pass

@dataclass
class Field:
    id_user: int
    name: str
    description: str
    location: List[int]
    data: Data
    img_path: str
    created_at: datetime = datetime.utcnow()
    edited_at: datetime = datetime.utcnow()

class FieldCreate(Field):
    id: int
    created_at: datetime = datetime.utcnow()
    edited_at: datetime = datetime.utcnow()