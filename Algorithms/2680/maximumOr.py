from itertools import accumulate
from operator import or_

class Solution:
    def maximumOr(self, nums: List[int], k: int) -> int:
        prefix_or = list(accumulate(nums, or_, initial=0))
        suffix_or = list(accumulate(reversed(nums), or_, initial=0))
        suffix_or.reverse()
        return max(prefix_or[i] | (nums[i] << k) | suffix_or[i + 1] for i in range(len(nums)))
