class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        l = r = 0
        while r < n:
            while r < n - 1 and nums[r] < nums[r + 1]:
                r += 1
            ans = max(ans, r - l + 1)
            l = r = r + 1
        return ans
