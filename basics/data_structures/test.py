from unittest import TestCase

from example import EXAMPLE_DATA
from example import get_friends_by_id as example_get_friends_by_id
from main import DATA, get_friends_by_id


class DataStructuresTest(TestCase):
    def test_function_core(self):
        for user_id in DATA.keys():
            res = get_friends_by_id(user_id, DATA)
            expected = example_get_friends_by_id(user_id, DATA)
            self.assertEqual(res, expected, "Working wrong")

        for user_id in EXAMPLE_DATA.keys():
            res = get_friends_by_id(user_id, EXAMPLE_DATA)
            expected = example_get_friends_by_id(user_id, EXAMPLE_DATA)
            self.assertEqual(res, expected, "Working wrong")

    def test_data_miss_user_id(self):
        with self.assertRaises(Exception, msg="You can receive id that is absent in data"):
            get_friends_by_id(100000, DATA)

    def test_returns_empty_list_if_not_friends(self):
        res = get_friends_by_id(1, {1: {"friends_ids": []}})
        self.assertEqual(res, [], "You should return empty list if user have no friends")

    def test_data_miss_friends_data(self):
        with self.assertRaises(Exception, msg="You can receive data with no friend data"):
            res = get_friends_by_id(1, {1: {"friends_ids": [2]}})
