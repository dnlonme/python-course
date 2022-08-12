from actions import *
from auth import get_current_user
from db import load_data, store_data
from utils import get_int_input

# Routing
ACTIONS = {
    1: get_list_action,
    2: get_todo_action,
    3: create_todo_action,
    4: update_todo_action,
    5: delete_todo_action,
    11: create_user_action,
    99: logout_action,
}

NO_AUTH_ACTIONS = {11, 99}


def main():
    load_data()
    while True:
        print("Available actions, type 0 to exit")
        for action_key, action in ACTIONS.items():
            print(f"{action_key}. {action}")
        user_action = get_int_input("Enter action you want to perform: ")
        if user_action == 0:
            break

        selected_action: Action = ACTIONS.get(user_action)
        if not selected_action:
            print("Invalid action number")
            continue
        if user_action in NO_AUTH_ACTIONS:
            selected_action.action()
            continue

        user = get_current_user()
        if not user:
            print("Authorization required to perform this action")
            select_user_to_authenticate()
            continue

        selected_action.action(user.id)
    print("Application closed")
    store_data()


if __name__ == "__main__":
    try:
        main()
    except BaseException as e:
        print(e)
        print("Unexpected error happened")
        store_data()
