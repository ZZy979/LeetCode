from collections import Counter

class Solution:
    def beautifulSubarrays(self, nums: List[int]) -> int:
        cnt = Counter([0])
        mask = ans = 0
        for x in nums:
            mask ^= x
            ans += cnt[mask]
            cnt[mask] += 1
        return ans
