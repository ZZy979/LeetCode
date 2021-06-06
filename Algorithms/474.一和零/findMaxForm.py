# 官方题解：动态规划
class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for s in strs:
            n0, n1 = count01(s)
            for j in range(m, n0 - 1, -1):
                for k in range(n, n1 - 1, -1):
                    dp[j][k] = max(dp[j][k], 1 + dp[j - n0][k - n1])
        return dp[m][n]


def count01(s):
    n0 = s.count('0')
    return n0, len(s) - n0
