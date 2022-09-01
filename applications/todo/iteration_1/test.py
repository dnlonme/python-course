from unittest import TestCase

from test_utils import TodoTestInputMockMixin

from .main import main


class TodoAppTest(TodoTestInputMockMixin, TestCase):
    def test_full_app(self):
        try:
            main()
        except SystemExit:
            pass
