# 单调栈
class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack = []
        ak = float('-inf')
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] < ak:
                return True
            while stack and nums[i] > stack[-1]:
                ak = stack.pop()
            stack.append(nums[i])
        return False
