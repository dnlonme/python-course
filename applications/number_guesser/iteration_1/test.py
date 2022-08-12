

from .main import main

from test_utils import NumberGuesserTest

PATH_PREFIX = __name__.replace('test', 'main') + '.'


class NumberGuesserTest1(NumberGuesserTest):

    @property
    def path_prefix(self):
        return PATH_PREFIX

    def test_game_success(self):
        self.randrange_mock.return_value = 1
        self.input_mock.return_value = '1'
        main()

        self.randrange_mock.assert_called_once()
        self.input_mock.assert_called_once()

        self.success_mock.assert_called_once()

        self.fail_mock.assert_not_called()

    def test_game_fail(self):
        self.randrange_mock.return_value = 2
        self.input_mock.return_value = '1'

        main()

        self.randrange_mock.assert_called_once()
        self.input_mock.assert_called_once()

        self.fail_mock.assert_called_once()

        self.success_mock.assert_not_called()
