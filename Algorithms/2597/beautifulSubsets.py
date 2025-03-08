from collections import Counter

# 回溯，时间复杂度O(2^n)，空间复杂度O(n)
class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        self.ans = 0
        self.backtrack(nums, k, 0, Counter())
        return self.ans - 1

    def backtrack(self, nums, k, i, subset):
        if i == len(nums):
            self.ans += 1
            return
        if not subset[nums[i] + k] and not subset[nums[i] - k]:
            subset[nums[i]] += 1
            self.backtrack(nums, k, i + 1, subset)
            subset[nums[i]] -= 1
        self.backtrack(nums, k, i + 1, subset)
