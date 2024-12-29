from collections import Counter

class Solution:
    def isPossibleToSplit(self, nums: List[int]) -> bool:
        return Counter(nums).most_common(1)[0][1] <= 2
