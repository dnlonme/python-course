from dataclasses import asdict, dataclass
from datetime import datetime
from typing import Callable

DATE_FORMAT = "%H:%M:%S %Y-%m-%d"


@dataclass
class BaseModel:
    id: int
    name: str
    created_at: datetime

    def to_dict(self) -> dict:
        data = asdict(self)
        data["created_at"] = self.created_at.strftime(DATE_FORMAT)
        return data

    @classmethod
    def from_json(cls, data: dict) -> "BaseModel":
        data["created_at"] = datetime.strptime(data["created_at"], DATE_FORMAT)
        return cls(**data)


@dataclass
class Todo(BaseModel):
    description: str
    is_completed: bool
    user_id: int

    def __str__(self):
        return f"{self.id}. {self.name} - {self.is_completed}"


@dataclass
class User(BaseModel):
    def __str__(self):
        return f"{self.id}. {self.name}"


@dataclass
class Action:
    id: int
    func: Callable[[], None]
    name: str

    def __str__(self):
        return f"{self.id}. {self.name}"


@dataclass
class TodoAction(Action):
    func: Callable[[int], None]


@dataclass
class UserAction(Action):
    func: Callable[[], User]
