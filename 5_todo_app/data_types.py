from dataclasses import dataclass, asdict
from datetime import datetime
from typing import Callable, Optional


DATE_FORMAT = '%H:%M:%S %Y-%m-%d'


@dataclass
class Todo:
    id: int
    name: str
    created_at: datetime
    is_finished: bool = False
    description: str = ''

    def __str__(self):
        text = ''
        for key, value in asdict(self).items():
            text += f'{key} : {value}, '
        return text

    def to_dict(self):
        data = asdict(self)
        data['created_at'] = self.created_at.strftime(DATE_FORMAT)
        return data


@dataclass
class Action:
    name: str
    action: Callable[[], None]

    def __str__(self):
        return self.name
