# 暴力法，时间复杂度O(n^4)，1560 ms
class Solution:
    def countQuadruplets(self, nums: List[int]) -> int:
        return sum(nums[a] + nums[b] + nums[c] == nums[d] for a in range(len(nums)) for b in range(a + 1, len(nums)) for c in range(b + 1, len(nums)) for d in range(c + 1, len(nums)))
