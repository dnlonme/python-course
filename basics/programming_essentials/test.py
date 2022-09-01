from unittest import TestCase

from example import ExampleSumMaster
from main import SumMaster


class SumMasterTest(TestCase):
    def test_all(self):
        sum_master = SumMaster(1)
        example_sum_master = ExampleSumMaster(1)
        self.assertEqual(sum_master.range_sum(11), sum(range(1, 11)), "Working wrong")
        self.assertEqual(sum_master.range_sum(11), example_sum_master.range_sum(11), "Working wrong")
