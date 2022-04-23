class Solution:
    def binaryGap(self, n: int) -> int:
        ans, last = 0, 31
        for i in range(32):
            if n & (1 << i):
                ans = max(ans, i - last)
                last = i
        return ans
