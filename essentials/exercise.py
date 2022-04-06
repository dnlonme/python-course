'''
    Create a class that will have methods to find sum of numbers between x and y
    class should receive minimum number as an instance attribute, and .range_sum method should receive maximum number,
    then you build range with this two numbers and sum it.

    Yeah, nothing crazy, just practice
'''
from example import ExampleSumMaster

TEST_MIN_NUMBER = 1
TEST_MAX_NUMBER = 11


class SumMaster:
    # write everything needed
    def __init__(self, range_min: int):
        self.min_number = range_min

    def range_sum(self, max_number: int) -> int:
        sum = 0
        for num in range(self.min_number, max_number):  # from 1 to 10
            sum += num
        return sum

# This will crush if you didn't write class properly, read the description
res = SumMaster(TEST_MIN_NUMBER).range_sum(TEST_MAX_NUMBER)
# Comparing your results to an example
assert res == ExampleSumMaster(TEST_MIN_NUMBER).range_sum(TEST_MAX_NUMBER), 'Your method is not working properly'
# Oh, by the way, we are testing code
assert res == sum(range(TEST_MIN_NUMBER, TEST_MAX_NUMBER)), 'Your method is not working properly'

# Are we implementing built-in functions?                                 Yes.
print('Done')
