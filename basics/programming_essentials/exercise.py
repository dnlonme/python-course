from example import ExampleSumMaster

TEST_MIN_NUMBER = 1
TEST_MAX_NUMBER = 11


class SumMaster:

    def __init__(self, min_number: int):
        '''Add min_number as an attribute of and object'''
        pass

    def range_sum(self, max_number: int) -> int:
        '''Return sum of numbers from min_number (you have it inside self) to max_number'''
        pass


# This will crush if you didn't write class properly, read the description
res = SumMaster(TEST_MIN_NUMBER).range_sum(TEST_MAX_NUMBER)
# Comparing your results to an example
assert res == ExampleSumMaster(TEST_MIN_NUMBER).range_sum(TEST_MAX_NUMBER), 'Your method is not working properly'
# Oh, by the way, we are testing code
assert res == sum(range(TEST_MIN_NUMBER, TEST_MAX_NUMBER)), 'Your method is not working properly'

# Are we implementing built-in functions?                                 Yes.
print('Done')
