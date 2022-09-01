from datetime import datetime

# List of todos. Each item is a dict with keys:
# id - int  (unique identifier for each item)
# name - string
# description - string
# is_completed - bool
# crated_at - datetime.datetime
DATA = [
    # Here's the example
    {
        "id": 1,
        "name": "wake up",
        "description": "try not to die",
        "is_completed": False,
        "created_at": datetime.now(),
    }
]


def main():
    pass


if __name__ == "__main__":
    main()
