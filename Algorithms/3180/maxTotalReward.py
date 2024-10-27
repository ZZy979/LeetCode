# 动态规划
class Solution:
    def maxTotalReward(self, rewardValues: List[int]) -> int:
        rewardValues.sort()
        m = rewardValues[-1]
        dp = [False] * (2 * m)
        dp[0] = True
        for x in rewardValues:
            for k in range(2 * x - 1, x - 1, -1):
                dp[k] |= dp[k - x]
        for i in range(len(dp) - 1, -1, -1):
            if dp[i]:
                break
        return i
