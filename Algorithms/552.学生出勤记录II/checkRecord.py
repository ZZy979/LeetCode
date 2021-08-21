# 官方题解1：动态规划
class Solution:
    def checkRecord(self, n: int) -> int:
        q = 10**9 + 7
        # dp[i][j][k]表示前i天有j个A且结尾有连续k个L的可奖励的出勤记录的数量
        dp = [[[0] * 3 for j in range(2)] for i in range(n + 1)]
        dp[0][0][0] = 1

        for i in range(1, n + 1):
            # 以P结尾的数量
            for j in range(2):
                for k in range(3):
                    dp[i][j][0] = (dp[i][j][0] + dp[i - 1][j][k]) % q
            # 以A结尾的数量
            for k in range(3):
                dp[i][1][0] = (dp[i][1][0] + dp[i - 1][0][k]) % q
            # 以L结尾的数量
            for j in range(2):
                for k in range(1, 3):
                    dp[i][j][k] = (dp[i][j][k] + dp[i - 1][j][k - 1]) % q
        total = sum(dp[n][j][k] for j in range(2) for k in range(3))
        return total % q
