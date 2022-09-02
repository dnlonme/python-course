from datetime import datetime
from typing import TypeVar

from .types import Todo

T = TypeVar("T")

# List of todos. Each item is a dict with keys:
# id - int  (unique identifier for each item)
# name - string
# description - string
# is_completed - bool
# crated_at - datetime.datetime
DATA = [
    # Here's the example
    Todo(id=1, name="wake up", description="try not to die", is_completed=False, created_at=datetime.now())
]


def get_user_int_input():
    pass


# This Typevar shows that we return an item which is of type that items of the list is.
def select_item(choices: list[T]) -> T:
    """Should handle selecting an item from given choices"""
    pass


def create_todo():
    pass


def update_todo():
    pass


def delete_todo():
    pass


def get_todo():
    pass


def list_todos():
    pass


def main():
    pass


if __name__ == "__main__":
    main()
