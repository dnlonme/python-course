import json

from applications.todo.iteration_7.example.models import Todo, User


def _load_data():
    with open("data.json", "rb") as f:
        if f.read(1):
            f.seek(0)
            data = json.load(f)
            if data:
                data = {
                    "todo": [Todo.from_json(todo) for todo in data["todo"]],
                    "user": [User.from_json(user) for user in data["user"]],
                }
                return data

        data = {"todo": [], "user": []}
    return data


def dump_data():
    with open("data.json", "w") as f:
        _data = {
            "todo": [todo.to_dict() for todo in DATA["todo"]],
            "user": [user.to_dict() for user in DATA["user"]],
        }
        data = json.dumps(_data)
        f.write(data)


DATA = _load_data()
