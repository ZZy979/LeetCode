import itertools

class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        n = len(nums)
        sums = list(itertools.accumulate(nums, initial=0))
        dp1 = [[0] * n for i in range(n)]
        dp2 = [[0] * n for i in range(n)]
        for i in range(n):
            dp2[i][i] = nums[i]
            if i < n - 1:
                dp1[i][i + 1] = max(nums[i], nums[i + 1])
        for r in range(1, n - 1, 2):
            for i in range(0, n - r):
                dp2[i][i + r] = sums[i + r + 1] - sums[i] - dp1[i][i + r]
            for i in range(0, n - r - 1):
                dp2[i][i + r + 1] = max(nums[i] + dp2[i + 1][i + r + 1], nums[i + r + 1] + dp2[i][i + r])
            for i in range(0, n - r - 1):
                dp1[i][i + r + 1] = sums[i + r + 2] - sums[i] - dp2[i][i + r + 1]
            for i in range(0, n - r - 2):
                dp1[i][i + r + 2] = max(nums[i] + dp1[i + 1][i + r + 2], nums[i + r + 2] + dp1[i][i + r + 1])
        return dp1[0][n - 1] * 2 >= sums[-1] if n % 2 == 0 else dp1[0][n - 1] * 2 <= sums[-1]
