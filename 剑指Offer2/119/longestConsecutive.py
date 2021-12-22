class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        ans = 0
        for x in nums:
            if x - 1 in nums:
                continue
            streak = 1
            while x + 1 in nums:
                x += 1
                streak += 1
            ans = max(ans, streak)
        return ans
