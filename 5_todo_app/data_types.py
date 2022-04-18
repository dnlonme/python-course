from dataclasses import dataclass
from typing import Callable


@dataclass
class Action:
    name: str
    action: Callable[[[]], None]

    def __str__(self):
        return self.name
