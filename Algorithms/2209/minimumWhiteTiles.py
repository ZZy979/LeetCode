# 官方题解：动态规划
class Solution:
    def minimumWhiteTiles(self, floor: str, numCarpets: int, carpetLen: int) -> int:
        n = len(floor)
        # dp[i][j]表示在前i个砖块上使用了j个地毯后，未被覆盖的白色砖块的最少数目
        dp = [[float('inf')] * (numCarpets + 1) for _ in range(n + 1)]
        for j in range(numCarpets + 1):
            dp[0][j] = 0
        for i in range(1, n + 1):
            dp[i][0] = dp[i - 1][0] + (floor[i - 1] == '1')
        for i in range(1, n + 1):
            for j in range(1, numCarpets + 1):
                dp[i][j] = min(dp[i - 1][j] + (floor[i - 1] == '1'), dp[max(0, i - carpetLen)][j - 1])
        return dp[n][numCarpets]
