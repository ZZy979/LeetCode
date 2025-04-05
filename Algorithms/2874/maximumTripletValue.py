from itertools import accumulate

class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        prefix_max = list(accumulate(nums, max))
        suffix_max = list(accumulate(reversed(nums), max))
        suffix_max.reverse()
        print(prefix_max)
        print(suffix_max)
        return max(0, max((prefix_max[j - 1] - nums[j]) * suffix_max[j + 1] for j in range(1, len(nums) - 1)))
