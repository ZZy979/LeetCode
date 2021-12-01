# 官方题解：dp[i][j]表示当数组剩下的部分为下标i到下标j时，当前玩家与另一个玩家的分数之差的最大值
class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        length = len(nums)
        if length % 2 == 0:
            return True
        dp = [0] * length
        for i, num in enumerate(nums):
            dp[i] = num
        for i in range(length - 2, -1, -1):
            for j in range(i + 1, length):
                dp[j] = max(nums[i] - dp[j], nums[j] - dp[j - 1])
        return dp[length - 1] >= 0
