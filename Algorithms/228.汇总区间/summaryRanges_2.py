class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        ans = []
        left = 0
        for i in range(len(nums)):
            if i == len(nums) - 1 or nums[i + 1] > nums[i] + 1:
                ans.append(str(nums[left]) + ('' if left == i else '->' + str(nums[i])))
                left = i + 1
        return ans
