# 暴力法，时间复杂度O(nk)
class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        return [
            nums[i + k - 1] if all(nums[j + 1] - nums[j] == 1 for j in range(i, i + k - 1)) else -1
            for i in range(n - k + 1)
        ]
