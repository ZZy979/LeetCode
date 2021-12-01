# 单调栈
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        next_greater = {}
        for x in nums2:
            while stack and stack[-1] < x:
                next_greater[stack.pop()] = x
            stack.append(x)
        return [next_greater.get(x, -1) for x in nums1]
