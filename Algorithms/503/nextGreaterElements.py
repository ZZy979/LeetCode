from itertools import chain

class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        stack, ans = [], [-1] * n
        for p, x in enumerate(chain(nums, nums)):
            while stack and stack[-1][1] < x:
                q, y = stack.pop()
                if q < n:
                    ans[q] = x
            stack.append((p, x))
        return ans
