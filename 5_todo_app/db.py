import json
from typing import Type
from models import Todo, User, BaseModel


DATA: dict[str, list[BaseModel]] = {
    'user': [],
    'todo': [],
}


def load_data():
    with open('data.json', 'r') as f:
        loaded_data: dict = json.load(f)
        models_mapping = {
            'user': User,
            'todo': Todo
        }
        for key, value in loaded_data.items():
            model = models_mapping[key]
            DATA[key] = [model.from_json(item) for item in value]


def store_data():
    for key, value in DATA.items():
        DATA[key] = [item.to_dict() for item in value]
    with open('data.json', 'w') as f:
        json.dump(DATA, f)


def get_data(user_id: int) -> list[Todo]:
    todos: list[Todo] = DATA.get('todo')
    result = list(filter(lambda todo: todo.user_id == user_id, todos))
    return result


def add_data(item: BaseModel):
    model_name = item.__class__.__name__.lower()
    model_data = DATA.get(model_name)
    model_data.append(item)


def update_data(item_to_update: Todo):
    model_name = item_to_update.__class__.__name__.lower()
    model_data = DATA.get(model_name)
    for item in model_data:
        if item.id == item_to_update.id:
            item.description = item_to_update.description
            item.is_finished = item_to_update.is_finished
            break


def remove_data(item: Todo):
    model_name = item.__class__.__name__.lower()
    model_data = DATA.get(model_name)
    model_data.remove(item)


def get_id(model_type: Type[BaseModel]) -> int:
    model_name = model_type.__name__.lower()
    model_data = DATA.get(model_name)
    if not model_data:
        return 1
    current_ids = [item.id for item in model_data]
    max_id = max(current_ids)
    return max_id + 1


def get_users():
    return DATA.get('user')
