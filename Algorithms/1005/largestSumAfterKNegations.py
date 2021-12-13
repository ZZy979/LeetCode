class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        nums.sort()
        m = sum(1 for x in nums if x < 0)
        if m == 0:
            return sum(nums) - 2 * nums[0] * (k % 2)
        # m > 0
        elif k < m:
            return sum(nums) - 2 * sum(nums[:k])
        # 0 < m <= k
        elif (k - m) % 2 == 0:
            return sum(nums) - 2 * sum(nums[:m])
        # 0 < m <= k, (k - m) % 2 == 1
        elif m < len(nums):
            return sum(nums) - 2 * sum(nums[:m]) - 2 * min(abs(nums[m - 1]), abs(nums[m]))
        # m == len(nums)
        else:
            return sum(nums) - 2 * sum(nums[:m]) - 2 * abs(nums[m - 1])
