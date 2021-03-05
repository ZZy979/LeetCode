class Solution:
    def cuttingRope(self, n: int) -> int:
        if n < 4:
            return n - 1
        ans = 1
        while n > 4:
            ans = ans * 3 % 1000000007
            n -= 3
        return ans * n % 1000000007
