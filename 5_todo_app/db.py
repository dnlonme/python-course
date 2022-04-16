import json
from dataclasses import asdict
from data_types import Todo, DATE_FORMAT
from datetime import datetime


DATA: list[Todo] = []


def load_data():
    with open('data.json', 'r') as f:
        loaded_data = json.load(f)
        for data in loaded_data:
            DATA.append(Todo.from_json(data))


def store_data():
    data_to_store = [item.to_dict() for item in DATA]
    with open('data.json', 'w') as f:
        json.dump(data_to_store, f)


def get_data() -> list[Todo]:
    return DATA


def add_data(item: Todo):
    DATA.append(item)


def update_data(item_to_update: Todo):
    for item in DATA:
        if item.id == item_to_update.id:
            item.description = item_to_update.description
            item.is_finished = item_to_update.is_finished
            break


def remove_data(item: Todo):
    DATA.remove(item)


def get_id() -> int:
    if not DATA:
        return 1
    current_ids = [item.id for item in DATA]
    max_id = max(current_ids)
    return max_id + 1
