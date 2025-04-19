from collections import Counter

class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        n = len(nums)
        cnt = Counter(nums[i] - i for i in range(n))
        return n * (n - 1) // 2 - sum(m * (m - 1) // 2 for m in cnt.values())
