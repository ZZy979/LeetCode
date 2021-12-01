import itertools

class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        n = len(nums)
        dp = [[0] * n for i in range(n)]
        for length in range(1, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                for m in range(i + 1, j):
                    dp[i][j] = max(dp[i][j], dp[i][m] + nums[i] * nums[m] * nums[j] + dp[m][j])
        return dp[0][n - 1]
