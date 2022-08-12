from typing import Type

from models import BaseModel


def get_int_input(console_text: str) -> int:
    try:
        user_input = int(input(console_text))
        return user_input
    except ValueError:
        print("Enter number")
        return get_int_input(console_text)


def get_bool_input(console_text: str) -> bool:
    user_input = get_int_input(console_text)
    if user_input not in range(2):
        print("Enter 1 or 0")
        return get_bool_input(console_text)
    return bool(user_input)


def get_choice(console_text: str, data: list) -> int:
    user_input = get_int_input(console_text)
    available_choices = get_available_choices(data)
    if user_input in available_choices:
        return user_input
    print("Invalid choice")
    return get_choice(console_text, data)


def get_available_choices(data: list) -> set[int]:
    return set(range(1, len(data) + 1))


def get_item_by_user_input(user_input: int, data: list[Type[BaseModel]]) -> Type[BaseModel]:
    return data[user_input - 1]
