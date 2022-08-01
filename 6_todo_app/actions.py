from datetime import datetime

from auth import authenticate_user, logout
from data_types import Action
from db import get_data, add_data, remove_data, get_id, update_data, get_users
from forms import todo_create_form, todo_update_form, user_create_form
from models import Todo, User
from utils import get_choice, get_item_by_user_input


# Service
def get_todo_list(user_id: int):
    for _id, todo in enumerate(get_data(user_id)):
        print(f'{_id + 1}. {todo.name} - {todo.is_finished}')


# Service
def select_item(console_text: str, user_id: int) -> Todo:
    get_todo_list(user_id)

    item_number = get_choice(console_text, get_data(user_id))
    item = get_item_by_user_input(item_number, get_data(user_id))
    return item


def create_todo(user_id: int):
    data = todo_create_form.get_data()
    todo = Todo(id=get_id(Todo), created_at=datetime.now(), user_id=user_id, **data)
    add_data(todo)


def delete_todo(user_id: int):
    item_to_delete = select_item("Enter item number you want to delete: ", user_id)
    remove_data(item_to_delete)


def update_todo(user_id: int):
    item_to_update = select_item("Enter item number you want to update: ", user_id)

    data = todo_update_form.get_data()
    item_to_update.__dict__.update(data)
    update_data(item_to_update)


def get_todo(user_id: int):
    item_to_show = select_item("Enter item number you want to see: ", user_id)
    print(item_to_show)


def create_user():
    data = user_create_form.get_data()
    user = User(id=get_id(User), created_at=datetime.now(), **data)
    add_data(user)


def list_users():
    users = get_users()
    if not users:
        print("No users created :(")
        create_user()

    for _id, user in enumerate(get_users()):
        print(f'{_id + 1}. {user.username}')


def select_user(console_text: str) -> User:
    list_users()

    item_number = get_choice(console_text, get_users())
    item = get_item_by_user_input(item_number, get_users())
    return item


def select_user_to_authenticate():
    user = select_user('Choose user to auth')
    authenticate_user(user)
    print(f'User: {user.username}')


# Views
get_list_action = Action(name='Get list', action=get_todo_list)
get_todo_action = Action(name='Get todo', action=get_todo)
create_todo_action = Action(name='Create todo', action=create_todo)
update_todo_action = Action(name='Update todo', action=update_todo)
delete_todo_action = Action(name='Delete todo', action=delete_todo)


create_user_action = Action(name='Create user', action=create_user)
logout_action = Action(name='Logout', action=logout)