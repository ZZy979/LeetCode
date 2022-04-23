class Solution:
    def binaryGap(self, n: int) -> int:
        ans, last, i = 0, 31, 0
        while n:
            if n & 1:
                ans = max(ans, i - last)
                last = i
            n >>= 1
            i += 1
        return ans
