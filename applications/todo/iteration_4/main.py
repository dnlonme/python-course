from datetime import datetime
from typing import TypeVar

from applications.todo.iteration_3.types import Action, Todo

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


def _select_todo() -> Todo:
    return select_item(DATA, "Select todo:\n")


def create_todo():
    name = input("Enter name:\n")
    description = input("Description:\n")
    _id = max([todo.id for todo in DATA]) + 1
    todo = Todo(id=_id, name=name, description=description, is_completed=False, created_at=datetime.now())
    DATA.append(todo)
    print(f"Todo {todo.name} created!")


def update_todo():
    todo = _select_todo()
    todo.is_completed = not todo.is_completed
    print(f"Todo {todo.name} is_completed is now {todo.is_completed}")


def delete_todo():
    todo = _select_todo()
    DATA.remove(todo)
    print(f"Todo with id {todo.id} was deleted")


def get_todo():
    todo = _select_todo()
    print(
        f"Name: {todo.name}\nDescription: {todo.description}\nCompleted:{todo.is_completed}\nCreated at: {todo.created_at}"
    )


def list_todos():
    for todo in DATA:
        print(str(todo))


ACTIONS = [
    Action(func=create_todo, name="create todo", id=1),
    Action(func=update_todo, name="update todo", id=2),
    Action(func=delete_todo, name="delete todo", id=3),
    Action(func=get_todo, name="get todo", id=4),
    Action(func=list_todos, name="list todos", id=5),
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
