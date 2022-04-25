from dataclasses import dataclass
from datetime import datetime
from typing import List

@dataclass
class Data:
    pass

@dataclass
class Field:
    id_user: int
    id_field: int
    name: str
    description: str
    data: Data
    created_at: datetime = datetime.utcnow()
    edited_at: datetime = datetime.utcnow()