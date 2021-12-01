class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = [[0] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = nums[i]
            if i < n - 1:
                dp[i][i + 1] = max(nums[i], nums[i + 1])
        for r in range(2, n):
            for i in range(n - r):
                j = i + r
                dp[i][j] = max(
                    nums[i] + min(dp[i + 1][j - 1], dp[i + 2][j]),
                    nums[j] + min(dp[i + 1][j - 1], dp[i][j - 2])
                )
        return dp[0][n - 1] >= sum(nums) / 2
