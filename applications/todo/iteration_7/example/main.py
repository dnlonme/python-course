import json
from datetime import datetime

from applications.todo.iteration_7.example.db import dump_data
from applications.todo.iteration_7.example.models import Action, TodoAction, UserAction
from applications.todo.iteration_7.example.todos_actions import TODO_ACTIONS
from applications.todo.iteration_7.example.users_actions import pick_user
from applications.todo.iteration_7.example.utils import finish_program, select_item

LOGOUT_ACTION = (UserAction(func=pick_user, name="logout", id=9),)
EXIT = (Action(func=finish_program, name="exit", id=0),)


def main():
    print("Welcome to the todo list!")
    user = pick_user()
    while True:
        action = select_item(TODO_ACTIONS + LOGOUT_ACTION + EXIT, "Pick an action:\n")
        if isinstance(action, TodoAction):
            action.func(user.id)
        elif isinstance(action, UserAction):
            user = action.func()
        else:
            action.func()  # logout
        input("Press Enter to continue:\n")


if __name__ == "__main__":
    try:
        main()
    except SystemExit:
        # if this exception is risen, then we've already dumped the data
        raise SystemExit
    except (Exception, KeyboardInterrupt) as e:
        print(e)
        dump_data()
