class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        for _ in range(k):
            i = nums.index(min(nums))
            nums[i] *= multiplier
        return nums
