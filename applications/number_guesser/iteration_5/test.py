from unittest.mock import patch

from test_utils import NumberGuesserTest

from .main import GuessGame

PATH_PREFIX = __name__.replace("test", "main") + "."

MAX_AMOUNT_OF_GUESSES = 11


class NumberGuesserTest4(NumberGuesserTest):
    @property
    def path_prefix(self):
        return PATH_PREFIX

    def _apply_patches(self):
        patches = super(NumberGuesserTest4, self)._apply_patches()
        next(patches)
        with patch(self.path_prefix + "game_over") as game_over_mock, patch(
            self.path_prefix + "wrong_input"
        ) as wrong_input_mock:
            self.game_over_mock = game_over_mock
            self.wrong_input_mock = wrong_input_mock
            yield
        next(patches)
        yield

    def test_game_success(self):
        self.randrange_mock.return_value = 1
        self.input_mock.return_value = "1"

        game = GuessGame(11, MAX_AMOUNT_OF_GUESSES)
        game.run()

        self.randrange_mock.assert_called_once()
        self.input_mock.assert_called_once()

        self.success_mock.assert_called_once()

        self.fail_mock.assert_not_called()

    def test_game_success_from_any_attempt(self):
        self.randrange_mock.return_value = 2
        self.input_mock.side_effect = ["1" for _ in range(MAX_AMOUNT_OF_GUESSES - 1)] + ["2"]

        game = GuessGame(11, MAX_AMOUNT_OF_GUESSES)
        game.run()

        self.randrange_mock.assert_called_once()
        self.assertEqual(self.input_mock.call_count, MAX_AMOUNT_OF_GUESSES)

        self.assertEqual(self.fail_mock.call_count, MAX_AMOUNT_OF_GUESSES - 1)

        self.success_mock.assert_called_once()

    def test_game_fail_and_continues(self):
        self.randrange_mock.return_value = 2
        self.input_mock.side_effect = ["1" for _ in range(MAX_AMOUNT_OF_GUESSES)]

        game = GuessGame(11, MAX_AMOUNT_OF_GUESSES)
        game.run()

        self.randrange_mock.assert_called_once()
        self.assertEqual(self.input_mock.call_count, MAX_AMOUNT_OF_GUESSES)

        self.assertEqual(self.fail_mock.call_count, MAX_AMOUNT_OF_GUESSES)

        self.success_mock.assert_not_called()

    def test_game_end_if_tries_exceeded(self):
        self.randrange_mock.return_value = 2
        self.input_mock.side_effect = ["1" for _ in range(MAX_AMOUNT_OF_GUESSES)]

        game = GuessGame(11, MAX_AMOUNT_OF_GUESSES)
        game.run()

        self.randrange_mock.assert_called_once()
        self.assertEqual(self.input_mock.call_count, MAX_AMOUNT_OF_GUESSES)

        self.assertEqual(self.fail_mock.call_count, MAX_AMOUNT_OF_GUESSES)

        self.success_mock.assert_not_called()

    def test_game_handles_wrong_input(self):
        self.randrange_mock.return_value = 2
        self.input_mock.side_effect = ["F"] + ["1" for _ in range(MAX_AMOUNT_OF_GUESSES)]

        game = GuessGame(11, MAX_AMOUNT_OF_GUESSES)
        game.run()

        self.randrange_mock.assert_called_once()
        self.wrong_input_mock.assert_called_once()
        self.assertEqual(self.input_mock.call_count, MAX_AMOUNT_OF_GUESSES + 1)

        self.assertEqual(self.fail_mock.call_count, MAX_AMOUNT_OF_GUESSES)

        self.success_mock.assert_not_called()
