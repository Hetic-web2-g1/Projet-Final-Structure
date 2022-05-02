from pydantic import BaseModel
from datetime import datetime


class EventCreate(BaseModel):
    id_user: int
    id_field: int
    name: str
    description: str
    subscripted_users: set


class Event(EventCreate):
    id: int
    created_at: datetime
    edited_at: datetime
