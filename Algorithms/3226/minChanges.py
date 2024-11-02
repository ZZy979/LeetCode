class Solution:
    def minChanges(self, n: int, k: int) -> int:
        ans = 0
        for i in range(20):
            if n & (1 << i) and not k & (1 << i):
                ans += 1
            elif not n & (1 << i) and k & (1 << i):
                return -1
        return ans
