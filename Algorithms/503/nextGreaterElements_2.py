class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        stack, ans = [], [-1] * n
        for i in range(2 * n):
            while stack and nums[stack[-1]] < nums[i % n]:
                ans[stack.pop()] = nums[i % n]
            stack.append(i % n)
        return ans
