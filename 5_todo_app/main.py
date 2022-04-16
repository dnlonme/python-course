from actions import *
from utils import get_int_input
from db import store_data, load_data


# Routing
ACTIONS = {
    1: get_list_action,
    2: get_todo_action,
    3: create_todo_action,
    4: update_todo_action,
    5: delete_todo_action,
}


def main():
    load_data()
    while True:
        print('Available actions, type 0 to exit')
        for action_key, action in ACTIONS.items():
            print(f'{action_key}. {action}')
        user_action = get_int_input('Enter action you want to perform: ')
        if user_action == 0:
            break
        selected_action: Action = ACTIONS.get(user_action)
        if not selected_action:
            print('Invalid action number')
            continue
        selected_action.action()
    print('Application closed')
    store_data()


if __name__ == '__main__':
    try:
        main()
    except BaseException as e:
        print(e)
        print('Unexpected error happened')
        store_data()
