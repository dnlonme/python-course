from unittest.mock import patch


class TodoTestInputMockMixin:

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

    def setUp(self) -> None:
        input_patch = patch("builtins.input")
        self.input_mock = input_patch.start()
        self.input_mock.side_effect = self.FLOW_INPUTS
        self.addCleanup(input_patch.stop)
