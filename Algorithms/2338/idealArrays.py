# 动态规划（超时），时间复杂度O(nM)，空间复杂度O(M)
class Solution:
    def idealArrays(self, n: int, maxValue: int) -> int:
        dp = [1] * (maxValue + 1)  # dp[j]表示以j结尾的理想数组数量
        q = 10**9 + 7
        for i in range(1, n):
            dp_new = [1] * (maxValue + 1)
            for j in range(2, maxValue + 1):
                for k in range(j, maxValue + 1, j):
                    dp_new[k] = (dp_new[k] + dp[j]) % q
            dp = dp_new
        return sum(dp[1:])
