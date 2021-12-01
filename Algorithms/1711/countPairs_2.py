from collections import Counter

# 官方题解
class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        max_sum = max(deliciousness) * 2
        count = Counter()
        ans = 0
        q = 10**9 + 7
        for i in deliciousness:
            s = 1
            while s <= max_sum:
                ans = (ans + count[s - i]) % q
                s <<= 1
            count[i] += 1
        return ans
