# 使用哈希表存储nums[d] - nums[c]，时间复杂度O(n²)，56 ms
class Solution:
    def countQuadruplets(self, nums: List[int]) -> int:
        ans = 0
        count = Counter()
        for b in range(len(nums) - 3, 0, -1):
            for d in range(b + 2, len(nums)):
                count[nums[d] - nums[b + 1]] += 1
            for a in range(b):
                ans += count[nums[a] + nums[b]]
        return ans
