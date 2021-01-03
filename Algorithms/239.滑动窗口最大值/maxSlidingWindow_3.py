# 官方题解3：分块+预处理
# 时间复杂度O(n)，空间复杂度O(n)
# 668 ms
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        prefixMax, suffixMax = [0] * n, [0] * n
        for i in range(n):
            if i % k == 0:
                prefixMax[i] = nums[i]
            else:
                prefixMax[i] = max(prefixMax[i - 1], nums[i])
        for i in range(n - 1, -1, -1):
            if i == n - 1 or (i + 1) % k == 0:
                suffixMax[i] = nums[i]
            else:
                suffixMax[i] = max(suffixMax[i + 1], nums[i])
        ans = [max(suffixMax[i], prefixMax[i + k - 1]) for i in range(n - k + 1)]
        return ans
