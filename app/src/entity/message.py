from dataclasses import dataclass
from datetime import datetime

@dataclass
class User:
    id_user: int | None
    id_field: int | None
    id_event: int | None
    message_type: str
    content: str
    created_at: datetime = datetime.utcnow()
    edited_at: datetime = datetime.utcnow()