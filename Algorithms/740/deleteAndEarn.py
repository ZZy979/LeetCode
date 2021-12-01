class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        total = [0] * (max(nums) + 1)
        for val in nums:
            total[val] += val
        
        dp = [0] * len(total)
        dp[0], dp[1] = total[0], max(total[0], total[1])
        for i in range(2, len(dp)):
            dp[i] = max(dp[i - 2] + total[i], dp[i - 1])
        return dp[-1]
