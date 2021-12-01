class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = [[]]
        for i in range(len(nums) - 1, -1, -1):
            for subset in ans.copy():
                ans.append([nums[i]] + subset)
        return ans
