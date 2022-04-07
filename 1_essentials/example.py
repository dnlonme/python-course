class ExampleSumMaster:

    def __init__(self, range_min: int):
        self.range_min = range_min

    def range_sum(self, range_max: int):
        sum = 0
        for num in range(self.range_min, range_max):
            sum += num
        return sum

