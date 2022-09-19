from datetime import datetime

from applications.todo.iteration_7.example.db import DATA
from applications.todo.iteration_7.example.models import Action, User, UserAction
from applications.todo.iteration_7.example.utils import (
    calculate_id,
    finish_program,
    select_item,
)


def _create_user() -> User:
    name = input("Enter user name:\n")

    _id = calculate_id("user")
    user = User(id=_id, name=name, created_at=datetime.now())
    DATA["user"].append(user)
    print(f"User {user.name} created!")
    return user


def _select_user() -> User:
    if not DATA["user"]:
        print("No users :( Create new one!")
        return _create_user()

    user = select_item(DATA["user"], "Select user:\n")
    return user


_USER_ACTIONS = [
    UserAction(name="Select existing user", func=_select_user, id=1),
    UserAction(name="Create new user", func=_create_user, id=2),
    Action(name="Exit", func=finish_program, id=0),
]


def pick_user() -> User:
    action = select_item(_USER_ACTIONS, "Pick action:\n")
    user = action.func()
    return user
