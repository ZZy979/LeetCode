from collections import Counter

# 滑动窗口，时间复杂度O(n)，空间复杂度O(n)
class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        m = len(set(nums))
        cnt = Counter()
        distinct = right = ans = 0
        for left in range(n):
            while right < n and distinct < m:
                if cnt[nums[right]] == 0:
                    distinct += 1
                cnt[nums[right]] += 1
                right += 1
            if distinct == m:
                ans += n - right + 1
            cnt[nums[left]] -= 1
            if cnt[nums[left]] == 0:
                distinct -= 1
            left += 1
        return ans
