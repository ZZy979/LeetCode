class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return binsearch(nums, target) - binsearch(nums, target - 1)


def binsearch(nums, x):
    left, right = 0, len(nums)
    while left < right:
        mid = (left + right) // 2
        if nums[mid] > x:
            right = mid
        else:
            left = mid + 1
    return left
