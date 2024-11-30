# 官方题解：动态规划，时间复杂度O(nm)，空间复杂度O(nm)
# 其中n是数组的长度，m是数组的最大值
class Solution:
    def countOfPairs(self, nums: List[int]) -> int:
        mod = 10**9 + 7
        n, m = len(nums), max(nums)
        # dp[i][j]表示当arr1[i]=j时，前i+1个元素组成的单调对的数目
        # dp[i][j] = sum(dp[i-1][k]), 0<=k<=j-d[i], d[i]=max{0,nums[i]-nums[i-1]}
        # => dp[i][j] = dp[i][j-1] + dp[i-1][j-d[i]]
        dp = [[0] * (m + 1) for _ in range(n)]
        for j in range(nums[0] + 1):
            dp[0][j] = 1
        for i in range(1, n):
            d = max(0, nums[i] - nums[i - 1])
            for j in range(d, nums[i] + 1):
                dp[i][j] = dp[i - 1][0] if j == 0 else (dp[i][j - 1] + dp[i - 1][j - d]) % mod
        return sum(dp[n - 1]) % mod
