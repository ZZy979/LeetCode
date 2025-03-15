class Solution:
    def sumOfBeauties(self, nums: List[int]) -> int:
        n = len(nums)
        beauty = [0] * n
        left_max = nums[0]
        right_min = nums[n - 1]
        for i in range(1, n - 1):
            beauty[i] = 2 if nums[i] > left_max else 1 if nums[i] > nums[i - 1] else 0
            left_max = max(left_max, nums[i])
        for i in range(n - 2, 0, -1):
            beauty[i] = min(beauty[i], 2 if nums[i] < right_min else 1 if nums[i] < nums[i + 1] else 0)
            right_min = min(right_min, nums[i])
        return sum(beauty)
