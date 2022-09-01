from unittest.mock import patch

FLOW_INPUTS = [
    5,
    "\n",
    1,
    "test",
    "test_description",
    2,
    2,
    "\n",
    4,
    2,
    "\n",
    3,
    2,
    "\n",
    5,
    "\n",
    0,
]


class TodoTestInputMockMixin:
    def setUp(self) -> None:
        input_patch = patch("builtins.input")
        input_mock = input_patch.start()
        input_mock.side_effect = FLOW_INPUTS
        self.addCleanup(input_patch.stop)
