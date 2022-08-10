from unittest import TestCase
from unittest.mock import Mock, patch
from main import main, success, fail, randrange


class NumberGuesserTest(TestCase):

    @patch('main.success')
    @patch('main.fail')
    @patch('main.randrange', return_value=1)
    @patch('main.input', return_value=1)
    def test_game_success(self, input_mock: Mock, randrange_mock: Mock, fail_mock: Mock, success_function_mock: Mock):

        main()

        randrange_mock.assert_called_once()
        input_mock.assert_called_once()

        success_function_mock.assert_called_once()

        fail_mock.assert_not_called()



