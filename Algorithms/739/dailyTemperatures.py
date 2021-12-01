class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        ans = [0] * len(temperatures)
        for i, t in enumerate(temperatures):
            while stack and stack[-1][1] < t:
                ans[stack[-1][0]] = i - stack[-1][0]
                stack.pop()
            stack.append((i, t))
        return ans
