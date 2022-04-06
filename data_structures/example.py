EXAMPLE_DATA = {
    5: {
        'name': "Pasha",
        'age': 50,
        'gender': 'old',
        'friends_ids': [6, 7]
    },
    6: {
        'name': "Stepan",
        'age': 21,
        'gender': 'male',
        'friends_ids': [5]
    },
    7: {
        'name': "Misha",
        'age': 23,
        'gender': 'male',
        'friends_ids': [6]
    }
}


def get_friends_by_id(user_id: int, data: dict) -> list[dict]:
    user_data = data.get(user_id)
    if not user_data:
        raise ValueError("Data doesn't contain given key")
    friends_ids = user_data.get('friends_ids')
    if not friends_ids:  # If list is empty, or absent
        return []
    result = []
    for friend_id in friends_ids:
        friend_data = data.get(friend_id)
        if not friend_data:
            raise ValueError(f"Friend with id {friend_id} doesn't exists in data")
        result.append(
            {
                'name': friend_data.get('name'),
                'age': friend_data.get('age'),
                'gender': friend_data.get('age'),
            }
        )
    return result
