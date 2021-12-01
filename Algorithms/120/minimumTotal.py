class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dp = [[0] * len(a) for a in triangle]
        dp[-1] = triangle[-1]
        for n in range(len(dp) - 2, -1, -1):
            for i in range(len(dp[n])):
                dp[n][i] = triangle[n][i] + min(dp[n + 1][i], dp[n + 1][i + 1])
        return dp[0][0]
