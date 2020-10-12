class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        if n < 2:
            return False
        s = sum(nums)
        if s % 2 == 1:
            return False
        target = s // 2
        if max(nums) > target:
            return False
        # dp[i][j]: 从数组的[0,i]下标范围内选取若干个正整数（可以是0个），是否存在一种选取方案使得被选取的正整数的和等于j
        dp = [[False] * (target + 1) for _ in range(n)]
        for i in range(n):
            dp[i][0] = True
        dp[0][nums[0]] = True
        for i in range(1, n):
            for j in range(1, target + 1):
                if j < nums[i]:
                    dp[i][j] = dp[i - 1][j]
                else:
                    dp[i][j] = dp[i - 1][j] or dp[i - 1][j - nums[i]]
        return dp[n - 1][target]
