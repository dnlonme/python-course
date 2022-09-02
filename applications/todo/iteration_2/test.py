from unittest import TestCase

from test_utils import TodoTestInputMockMixin

from .main import main


class TodoAppTest(TodoTestInputMockMixin, TestCase):
    def test_full_app(self):
        try:
            main()
        except SystemExit:
            pass
        self.assertEquals(
            len(self.input_mock.mock_calls),
            len(self.FLOW_INPUTS),
            msg="Input should be called the same amount of times as len of FLOW_INPUTS",
        )
