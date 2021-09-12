# 官方题解：动态规划
class Solution:
    def findIntegers(self, n: int) -> int:
        dp = [0] * 31
        dp[0] = dp[1] = 1
        for i in range(2, 31):
            dp[i] = dp[i - 1] + dp[i - 2]

        pre = res = 0
        for i in range(29, -1, -1):
            if n & (1 << i):
                res += dp[i + 1]
                if pre == 1:
                    break
                pre = 1
            else:
                pre = 0
            if i == 0:
                res += 1
        return res
