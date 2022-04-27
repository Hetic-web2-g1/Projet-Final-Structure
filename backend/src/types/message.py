from datetime import datetime
from pydantic import BaseModel


class MessageCreate(BaseModel):
    id_user: int | None
    id_field: int | None
    id_event: int | None
    message_type: str
    content: str


class Message(MessageCreate):
    id: int
    created_at: datetime
    edited_at: datetime
