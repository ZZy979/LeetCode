# 评论区解法
class Solution:
    def clumsy(self, N: int) -> int:
        if N <= 2:
            return N
        elif N == 3:
            return 6
        ans = N * (N - 1) // (N - 2) + N - 3
        N -= 4
        while N >= 4:
            ans += -(N * (N - 1) // (N - 2)) + N - 3
            N -= 4
        return ans - self.clumsy(N)
