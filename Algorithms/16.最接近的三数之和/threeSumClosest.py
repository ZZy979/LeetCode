class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        n = len(nums)
        nums.sort()
        closest = nums[0] + nums[1] + nums[-1]
        for i in range(n - 2):
            left, right = i + 1, n - 1
            while left < right:
                s = nums[i] + nums[left] + nums[right]
                if abs(s - target) < abs(closest - target):
                    closest = s
                if s > target:
                    right -= 1
                elif s < target:
                    left += 1
                else:
                    return s
        return closest
