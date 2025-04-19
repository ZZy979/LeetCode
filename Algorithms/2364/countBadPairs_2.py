from collections import Counter

class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        cnt = Counter()
        res = 0
        for i, x in enumerate(nums):
            res += i - cnt[x - i]
            cnt[x - i] += 1
        return res
