class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [0] * (target + 1)
        dp[0] = 1
        for t in range(1, target + 1):
            for x in nums:
                if t >= x:
                    dp[t] += dp[t - x]
        return dp[target]
