# 方法1：迭代
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = [[]]
        for n in nums:
            for i in range(len(ans)):
                ans.append(ans[i] + [n])
        return ans
