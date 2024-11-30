# 官方题解一：动态规划，时间复杂度O(nm²)，空间复杂度O(nm)
# 其中n是数组的长度，m是数组的最大值
class Solution:
    def countOfPairs(self, nums: List[int]) -> int:
        n = len(nums)
        # dp[i][j]表示当arr1[i]=j时，前i+1个元素组成的单调对的数目
        # dp[i][j] = sum(dp[i-1][k]), k<=j且0<=nums[i]-j<=nums[i-1]-k
        dp = [[0] * 51 for _ in range(n)]
        mod = 10**9 + 7
        for j in range(nums[0] + 1):
            dp[0][j] = 1
        for i in range(1, n):
            for j in range(nums[i] + 1):
                dp[i][j] = sum(dp[i - 1][k] for k in range(j + 1) if nums[i - 1] - k >= nums[i] - j) % mod
        return sum(dp[n - 1]) % mod
