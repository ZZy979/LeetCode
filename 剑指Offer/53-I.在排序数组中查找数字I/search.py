import bisect

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return bisect.bisect_right(nums, target) - bisect.bisect_left(nums, target)
