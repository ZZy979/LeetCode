from collections import Counter

# 滑动窗口（双指针），时间复杂度O(n)，空间复杂度O(n)
class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        n = len(nums)
        cnt = Counter()
        num_equal_pairs = right = ans = 0
        for left in range(n):
            while right < n and num_equal_pairs < k:
                num_equal_pairs += cnt[nums[right]]
                cnt[nums[right]] += 1
                right += 1
            if num_equal_pairs >= k:
                ans += n - right + 1
            cnt[nums[left]] -= 1
            num_equal_pairs -= cnt[nums[left]]
        return ans
