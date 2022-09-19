from typing import TypeVar

from applications.todo.iteration_7.example.db import DATA, dump_data

T = TypeVar("T")


def finish_program():
    dump_data()
    exit()


def _get_user_int_input(text: str):
    try:
        user_input = int(input(text))
        return user_input
    except ValueError:
        print("Please enter a number")
        return _get_user_int_input(text)


def select_item(choices: list[T], text: str) -> T:
    """Should return index pos of selected string"""
    for item in choices:
        print(str(item))

    choice_id = _get_user_int_input(text)
    res = list(filter(lambda x: x.id == choice_id, choices))
    if not res:
        print(f"{choice_id} isn't a valid choice")
        return select_item(choices, text)
    return res[0]


def calculate_id(model_name: str) -> int:
    if DATA[model_name]:
        _id = max([todo.id for todo in DATA[model_name]]) + 1
    else:
        _id = 1
    return _id
