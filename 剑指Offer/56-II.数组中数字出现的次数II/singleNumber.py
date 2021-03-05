from collections import Counter

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        count = Counter(nums)
        for k in count:
            if count[k] == 1:
                return k
