from datetime import datetime
from typing import TypeVar

from .types import Action, Todo

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


def get_user_int_input(text: str):
    pass


def select_item(choices: list[T], text: str) -> T:
    """Should return item from choices"""
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


ACTIONS = [
    Action(func=exit, name="exit", id=0),
]


def main():
    print("Welcome to the todo list!")
    while True:
        action = select_item(ACTIONS, "Pick an action:\n")
        action.func()
        input("Press Enter to continue:\n")


if __name__ == "__main__":
    main()
