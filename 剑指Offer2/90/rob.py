class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 3:
            return max(nums, default=0)
        # 不偷n-1号，等价于0~n-2号无环
        dp = [0] * (n - 1)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, n - 1):
            dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])
        # 不偷0号，等价于1~n-1号无环
        dp2 = [0] * n
        dp2[1] = nums[1]
        dp2[2] = max(nums[1], nums[2])
        for i in range(3, n):
            dp2[i] = max(dp2[i - 2] + nums[i], dp2[i - 1])
        return max(dp[n - 2], dp2[n - 1])
