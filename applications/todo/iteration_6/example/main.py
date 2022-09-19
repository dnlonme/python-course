import json
from datetime import datetime
from typing import TypeVar

from applications.todo.iteration_6.example.models import Action, Todo, User

T = TypeVar("T")


# List of todos. Each item is a dict with keys:
# id - int  (unique identifier for each item)
# name - string
# description - string
# is_completed - bool
# crated_at - datetime.datetime


# You should initialize DATA variable yourself
DATA = {}


def load_data():
    global DATA
    with open("data.json", "rb") as f:
        if f.read(1):
            f.seek(0)
            data = json.load(f)
            if data:
                DATA = {
                    "todo": [Todo.from_json(todo) for todo in data["todo"]],
                    "user": [User.from_json(user) for user in data["user"]],
                }
                return

        DATA = {"todo": [], "user": []}


def dump_data():
    with open("data.json", "w") as f:
        _data = {
            "todo": [todo.to_dict() for todo in DATA["todo"]],
            "user": [user.to_dict() for user in DATA["user"]],
        }
        data = json.dumps(_data)
        f.write(data)


def _exit():
    dump_data()
    exit()


def get_user_int_input(text: str):
    try:
        user_input = int(input(text))
        return user_input
    except ValueError:
        print("Please enter a number")
        return get_user_int_input(text)


def select_item(choices: list[T], text: str) -> T:
    """Should return index pos of selected string"""
    for item in choices:
        print(str(item))

    choice_id = get_user_int_input(text)
    res = list(filter(lambda x: x.id == choice_id, choices))
    if not res:
        print(f"{choice_id} isn't a valid choice")
        return select_item(choices, text)
    return res[0]


def create_user() -> User:
    name = input("Enter user name:\n")
    if DATA["user"]:
        _id = max([todo.id for todo in DATA["user"]]) + 1
    else:
        _id = 1
    user = User(id=_id, name=name, created_at=datetime.now())
    DATA["user"].append(user)
    print(f"User {user.name} created!")
    return user


def select_user() -> User:
    if not DATA["user"]:
        print("No users :( Create new one!")
        return create_user()

    user = select_item(DATA["user"], "Select user:\n")
    return user


USER_ACTIONS = [
    Action(name="Select existing user", func=select_user, id=1),
    Action(name="Create new user", func=create_user, id=2),
    Action(name="Exit", func=_exit, id=0),
]


def pick_user() -> int:
    action = select_item(USER_ACTIONS, "Pick action:\n")
    user = action.func()
    return user.id


def select_todo(user_id: int) -> Todo:
    return select_item(list(filter(lambda todo: todo.user_id == user_id, DATA["todo"])), "Select todo:\n")


def create_todo(user_id: int):
    name = input("Enter name:\n")
    description = input("Description:\n")
    if DATA["todo"]:
        _id = max([todo.id for todo in DATA["todo"]]) + 1
    else:
        _id = 1
    todo = Todo(
        id=_id,
        name=name,
        description=description,
        is_completed=False,
        created_at=datetime.now(),
        user_id=user_id,
    )
    DATA["todo"].append(todo)
    print(f"Todo {todo.name} created!")


def update_todo(user_id: int):
    todo = select_todo(user_id)
    todo.is_completed = not todo.is_completed
    print(f"Todo {todo.name} is_completed is now {todo.is_completed}")


def delete_todo(user_id: int):
    todo = select_todo(user_id)
    DATA["todo"].remove(todo)
    print(f"Todo with id {todo.id} was deleted")


def get_todo(user_id: int):
    todo = select_todo(user_id)
    print(
        f"Name: {todo.name}\nDescription: {todo.description}\nCompleted:{todo.is_completed}\nCreated at: {todo.created_at}"
    )


def list_todos(user_id: int):
    for todo in filter(lambda todo: todo.user_id == user_id, DATA["todo"]):
        print(str(todo))


TODO_ACTIONS = [
    Action(func=create_todo, name="create todo", id=1),
    Action(func=update_todo, name="update todo", id=2),
    Action(func=delete_todo, name="delete todo", id=3),
    Action(func=get_todo, name="get todo", id=4),
    Action(func=list_todos, name="list todos", id=5),
    Action(func=pick_user, name="logout", id=9),
    Action(func=_exit, name="exit", id=0),
]


def main():
    load_data()
    print("Welcome to the todo list!")
    user_id = pick_user()
    while True:
        action = select_item(TODO_ACTIONS, "Pick an action:\n")
        if action.id == 0:
            action.func()
        if action.id == 9:
            user_id = action.func()
            continue
        action.func(user_id)
        input("Press Enter to continue:\n")


if __name__ == "__main__":
    try:
        main()
    except SystemExit:
        # if this exception is risen, then we've already dumped the data
        raise SystemExit
    except (Exception, KeyboardInterrupt) as e:
        print(e)
        dump_data()
