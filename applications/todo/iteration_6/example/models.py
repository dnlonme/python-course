from dataclasses import asdict, dataclass
from datetime import datetime
from typing import Callable

DATE_FORMAT = "%H:%M:%S %Y-%m-%d"


@dataclass
class Todo:
    id: int
    name: str
    description: str
    is_completed: bool
    user_id: int
    created_at: datetime

    def __str__(self):
        return f"{self.id}. {self.name} - {self.is_completed}"

    def to_dict(self):
        data = asdict(self)
        data["created_at"] = self.created_at.strftime(DATE_FORMAT)
        return data

    @classmethod
    def from_json(cls, data: dict) -> "Todo":
        data["created_at"] = datetime.strptime(data["created_at"], DATE_FORMAT)
        return cls(**data)


@dataclass
class User:
    id: int
    name: str
    created_at: datetime

    def __str__(self):
        return f"{self.id}. {self.name}"

    def to_dict(self):
        data = asdict(self)
        data["created_at"] = self.created_at.strftime(DATE_FORMAT)
        return data

    @classmethod
    def from_json(cls, data: dict) -> "User":
        data["created_at"] = datetime.strptime(data["created_at"], DATE_FORMAT)
        return cls(**data)


@dataclass
class Action:
    id: int
    func: Callable
    name: str

    def __str__(self):
        return f"{self.id}. {self.name}"
