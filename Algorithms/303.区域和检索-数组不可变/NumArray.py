from itertools import accumulate

class NumArray:

    def __init__(self, nums: List[int]):
        self.sums = list(accumulate(nums, initial=0))

    def sumRange(self, i: int, j: int) -> int:
        return self.sums[j + 1] - self.sums[i]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)
