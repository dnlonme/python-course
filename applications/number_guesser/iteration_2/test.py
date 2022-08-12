import os
from functools import partial
from unittest.mock import patch

from test_utils import NumberGuesserTest

from .main import main

PATH_PREFIX = __name__.replace("test", "main") + "."


class LoopLimiter:
    def __init__(self, amount_of_iterations: int):
        self.current_iterations = 0
        self.amount_of_iterations = amount_of_iterations

    def __call__(self, *args, **kwargs):
        self.current_iterations += 1
        return self.current_iterations <= self.amount_of_iterations


class NumberGuesserTest2(NumberGuesserTest):

    loop_count = 3

    @property
    def path_prefix(self):
        return PATH_PREFIX

    def test_game_success(self):
        self.randrange_mock.return_value = 1
        self.input_mock.return_value = "1"
        main()

        self.randrange_mock.assert_called_once()
        self.input_mock.assert_called_once()

        self.success_mock.assert_called_once()

        self.fail_mock.assert_not_called()

    def test_game_success_from_any_attempt(self):
        with patch(self.path_prefix + "loop_condition", LoopLimiter(self.loop_count)):
            self.randrange_mock.return_value = 2
            self.input_mock.side_effect = ["1" for _ in range(self.loop_count - 1)] + ["2"]

            main()

            self.randrange_mock.assert_called_once()
            self.assertEqual(self.input_mock.call_count, self.loop_count)

            self.assertEqual(self.fail_mock.call_count, self.loop_count - 1)

            self.success_mock.assert_called_once()

    def test_game_fail_and_continues(self):
        with patch(self.path_prefix + "loop_condition", LoopLimiter(self.loop_count)):
            self.randrange_mock.return_value = 2
            self.input_mock.side_effect = ["1" for _ in range(self.loop_count)]

            main()

            self.randrange_mock.assert_called_once()
            self.assertEqual(self.input_mock.call_count, self.loop_count)

            self.assertEqual(self.fail_mock.call_count, self.loop_count)

            self.success_mock.assert_not_called()
