# 使用哈希表存储nums[d]，时间复杂度O(n³)，224 ms
class Solution:
    def countQuadruplets(self, nums: List[int]) -> int:
        ans = 0
        count = Counter()
        for c in range(len(nums) - 2, 1, -1):
            count[nums[c + 1]] += 1
            for a in range(c):
                for b in range(a + 1, c):
                    ans += count[nums[a] + nums[b] + nums[c]]
        return ans
