class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if not nums:
            return 0
        n = len(nums)
        left = right = 0
        t = 0
        ans = n + 1
        while right < n:
            t += nums[right]
            while t >= target:
                ans = min(ans, right - left + 1)
                t -= nums[left]
                left += 1
            right += 1
        return 0 if ans == n + 1 else ans
