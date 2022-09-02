from dataclasses import dataclass
from datetime import datetime


@dataclass
class Todo:
    id: int
    name: str
    description: str
    is_completed: bool
    created_at: datetime
