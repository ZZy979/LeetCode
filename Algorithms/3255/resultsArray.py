# 统计长度，时间复杂度O(n)
class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        ans = []
        count = 1
        for i in range(len(nums)):
            count = count + 1 if i > 0 and nums[i] - nums[i - 1] == 1 else 1
            if i >= k - 1:
                ans.append(nums[i] if count >= k else -1)
        return ans
