# 评论区解法：中心扩展法
class Solution:
    def minCut(self, s: str) -> int:
        if len(s) <= 1:
            return 0
        n = len(s)
        dp = [9999] * n
        for i in range(n):
            helper(s, i, i, dp)
            helper(s, i, i + 1, dp)
        return dp[n - 1]


def helper(s, i, j, dp):
    while i >= 0 and j < len(s) and s[i] == s[j]:
        dp[j] = min(dp[j], 0 if i == 0 else dp[i - 1] + 1)
        i -= 1
        j += 1
