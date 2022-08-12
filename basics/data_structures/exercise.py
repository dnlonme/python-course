"""Write a function that will take user id and return names, age and gender of his friends, as a list of dicts"""
from example import EXAMPLE_DATA
from example import get_friends_by_id as example_get_friends_by_id

DATA = {
    0: {"name": "Pasha", "age": 50, "gender": "old", "friends_ids": [1, 2]},
    1: {"name": "Stepan", "age": 21, "gender": "male", "friends_ids": [0]},
    2: {"name": "Misha", "age": 23, "gender": "male", "friends_ids": [1]},
}


def get_friends_by_id(user_id: int, data: dict) -> list[dict]:
    pass


# res = get_friends_by_id(0, DATA)
# res [{'name': "Stepan", 'age': 21, 'gender': 'fluid'}]


for user_id in DATA.keys():
    res = get_friends_by_id(user_id, DATA)
    expected = example_get_friends_by_id(user_id, DATA)
    assert res == expected, "Working wrong"

for user_id in EXAMPLE_DATA.keys():
    res = get_friends_by_id(user_id, EXAMPLE_DATA)
    expected = example_get_friends_by_id(user_id, EXAMPLE_DATA)
    assert res == expected, "Working wrong"

print("Working properly")
