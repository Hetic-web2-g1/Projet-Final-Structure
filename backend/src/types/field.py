from datetime import datetime
from typing import List

from pydantic import BaseModel


class FieldCreate(BaseModel):
    id_user: int
    name: str
    description: str
    location: List[int]
    img_path: str
    created_at: datetime
    edited_at: datetime


class Field(FieldCreate):
    id: int
    created_at: datetime
    edited_at: datetime
