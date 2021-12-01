import itertools

class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        n = len(nums)
        # dp[i][j]: nums[:i]分成j组，各组和最大值的最小值
        dp = [[0] * (m + 1) for i in range(n + 1)]
        sums = list(itertools.accumulate(nums, initial=0))
        for i in range(1, n + 1):
            dp[i][1] = sums[i]
        for j in range(2, m + 1):
            for i in range(j, n + 1):
                dp[i][j] = min(max(dp[k][j - 1], sums[i] - sums[k]) for k in range(1, i))
        return dp[n][m]
