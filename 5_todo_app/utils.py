from data_types import Todo


def get_int_input(console_text: str) -> int:
    try:
        user_input = int(input(console_text))
        return user_input
    except ValueError:
        print('Enter number')
        return get_int_input(console_text)


def get_choice(console_text: str, data: list) -> int:
    user_input = get_int_input(console_text)
    available_choices = get_available_choices(data)
    if user_input in available_choices:
        return user_input
    print('Invalid choice')
    return get_choice(console_text, data)


def get_available_choices(data: list) -> set[int]:
    return set(range(1, len(data) + 1))


def get_item_by_user_input(user_input: int, data: list[Todo]) -> Todo:
    return data[user_input - 1]

