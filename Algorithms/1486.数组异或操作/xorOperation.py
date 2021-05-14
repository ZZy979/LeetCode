class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        ans = x = start
        for i in range(n - 1):
            x += 2
            ans ^= x
        return ans
