# 动态规划
class Solution:
    def knightDialer(self, n: int) -> int:
        q = 10**9 + 7
        dp = [1] * 10
        move = [(4, 6), (6, 8), (7, 9), (4, 8), (0, 3, 9), (), (0, 1, 7), (2, 6), (1, 3), (2, 4)]
        for _ in range(n - 1):
            dp = [sum((dp[j] for j in move[i]), start=0) % q for i in range(10)]
        return sum(dp) % q
