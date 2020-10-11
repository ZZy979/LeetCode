from itertools import accumulate

class NumArray:

    def __init__(self, nums: List[int]):
        self.sums = list(accumulate(nums))

    def sumRange(self, i: int, j: int) -> int:
        return self.sums[j] if i == 0 else self.sums[j] - self.sums[i - 1]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)
