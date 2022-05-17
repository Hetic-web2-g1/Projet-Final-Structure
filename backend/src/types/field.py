from datetime import datetime
from typing import List
from pydantic import BaseModel
from uuid import UUID


class FieldCreate(BaseModel):
    id_user: UUID
    name: str
    description: str
    location: List[int]
    img_path: str
    created_at: datetime
    edited_at: datetime


class Field(FieldCreate):
    id: UUID
    created_at: datetime
    edited_at: datetime
