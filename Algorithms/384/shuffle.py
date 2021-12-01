from random import shuffle

class Solution:

    def __init__(self, nums: List[int]):
        self.original = nums
        self.nums = nums.copy()

    def reset(self) -> List[int]:
        return self.original

    def shuffle(self) -> List[int]:
        shuffle(self.nums)
        return self.nums


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()
