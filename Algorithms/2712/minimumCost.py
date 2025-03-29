# 动态规划
class Solution:
    def minimumCost(self, s: str) -> int:
        n = len(s)
        prefix = [0] * n  # prefix[i]表示将s[0..i-1]全部变为s[i]的最小成本
        suffix = [0] * n  # suffix[i]表示将s[i+1..n-1]全部变为s[i]的最小成本
        for i in range(1, n):
            prefix[i] = prefix[i - 1] if s[i] == s[i - 1] else prefix[i - 1] + i
        for i in range(n - 2, -1, -1):
            suffix[i] = suffix[i + 1] if s[i] == s[i + 1] else suffix[i + 1] + n - i - 1
        return min(prefix[i] + suffix[i] for i in range(n))
