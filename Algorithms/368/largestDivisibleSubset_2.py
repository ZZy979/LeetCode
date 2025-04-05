# 官方题解：动态规划
class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        n = len(nums)
        nums.sort()

        dp = [1] * n  # dp[i]表示在nums升序排列的前提下，以nums[i]为最大整数的整除子集的大小
        max_size = max_val = 1
        for i in range(1, n):
            for j in range(i):
                if nums[i] % nums[j] == 0:
                    dp[i] = max(dp[i], dp[j] + 1)
            if dp[i] > max_size:
                max_size, max_val = dp[i], nums[i]
        
        if max_size == 1:
            return [nums[0]]
        ans = []
        for i in range(n - 1, -1, -1):
            if max_size == 0:
                break
            if dp[i] == max_size and max_val % nums[i] == 0:
                ans.append(nums[i])
                max_val = nums[i]
                max_size -= 1
        return ans
