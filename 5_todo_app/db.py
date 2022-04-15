import json
from dataclasses import asdict
from data_types import Todo, DATE_FORMAT
from datetime import datetime


DATA: list[Todo] = []


def load_data():
    with open('data.json', 'r') as f:
        loaded_data = json.load(f)
        for data in loaded_data:
            data['created_at'] = datetime.strptime(data['created_at'], DATE_FORMAT)
            DATA.append(Todo(**data))


def store_data():
    data_to_store = [item.to_dict() for item in DATA]
    with open('data.json', 'w') as f:
        json.dump(data_to_store, f)


def get_data() -> list[Todo]:
    return DATA


def add_data(item: Todo):
    DATA.append(item)


def remove_data(item: Todo):
    DATA.remove(item)


def get_id() -> int:
    if not DATA:
        return 1
    current_ids = [item.id for item in DATA]
    max_id = max(current_ids)
    return max_id + 1
