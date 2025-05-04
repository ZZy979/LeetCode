# 滑动窗口，时间复杂度O(n)，空间复杂度O(1)
class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        n, m = len(nums), max(nums)
        count = right = ans = 0
        for left in range(n):
            while right < n and count < k:
                if nums[right] == m:
                    count += 1
                right += 1
            if count == k:
                ans += n - right + 1
            if nums[left] == m:
                count -= 1
        return ans
