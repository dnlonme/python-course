from datetime import datetime

from applications.todo.iteration_7.example.db import DATA
from applications.todo.iteration_7.example.models import Todo, TodoAction
from applications.todo.iteration_7.example.utils import calculate_id, select_item


def _select_todo(user_id: int) -> Todo:
    return select_item(list(filter(lambda todo: todo.user_id == user_id, DATA["todo"])), "Select todo:\n")


def _create_todo(user_id: int):
    name = input("Enter name:\n")
    description = input("Description:\n")
    todo = Todo(
        id=calculate_id("todo"),
        name=name,
        description=description,
        is_completed=False,
        created_at=datetime.now(),
        user_id=user_id,
    )
    DATA["todo"].append(todo)
    print(f"Todo {todo.name} created!")


def _update_todo(user_id: int):
    todo = _select_todo(user_id)
    todo.is_completed = not todo.is_completed
    print(f"Todo {todo.name} is_completed is now {todo.is_completed}")


def _delete_todo(user_id: int):
    todo = _select_todo(user_id)
    DATA["todo"].remove(todo)
    print(f"Todo with id {todo.id} was deleted")


def _get_todo(user_id: int):
    todo = _select_todo(user_id)
    print(
        f"Name: {todo.name}\nDescription: {todo.description}\nCompleted:{todo.is_completed}\nCreated at: {todo.created_at}"
    )


def _list_todos(user_id: int):
    for todo in filter(lambda todo: todo.user_id == user_id, DATA["todo"]):
        print(str(todo))


TODO_ACTIONS = [
    TodoAction(func=_create_todo, name="create todo", id=1),
    TodoAction(func=_update_todo, name="update todo", id=2),
    TodoAction(func=_delete_todo, name="delete todo", id=3),
    TodoAction(func=_get_todo, name="get todo", id=4),
    TodoAction(func=_list_todos, name="list todos", id=5),
]
