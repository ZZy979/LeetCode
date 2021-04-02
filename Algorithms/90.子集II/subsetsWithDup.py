class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = [[]]
        left, right, length = 0, 1, 0
        for i in range(len(nums)):
            left = len(ans) - length if i > 0 and nums[i] == nums[i - 1] else 0
            right = len(ans)
            length = right - left
            for j in range(left, right):
                ans.append(ans[j] + [nums[i]])
        return ans
