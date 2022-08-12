from abc import ABC, abstractmethod
from functools import partial
from unittest import TestCase
from unittest.mock import patch


class NumberGuesserTest(TestCase, ABC):
    def setUp(self) -> None:
        patch_generator = self._apply_patches()
        next(patch_generator)
        self.addCleanup(partial(next, patch_generator))

    def _apply_patches(self):
        with patch(self.path_prefix + "success") as success_mock, patch(
            self.path_prefix + "fail"
        ) as fail_mock, patch(self.path_prefix + "randrange") as randrange_mock, patch(
            self.path_prefix + "input"
        ) as input_mock:
            self.success_mock = success_mock
            self.fail_mock = fail_mock
            self.randrange_mock = randrange_mock
            self.input_mock = input_mock
            yield
        yield

    @property
    @abstractmethod
    def path_prefix(self) -> str:
        pass
