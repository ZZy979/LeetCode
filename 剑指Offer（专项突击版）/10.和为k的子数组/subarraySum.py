from collections import Counter

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        ans = pre = 0
        c = Counter([0])
        for x in nums:
            pre += x
            ans += c[pre - k]
            c[pre] += 1
        return ans
