class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = []
        mark = [0] * len(s)
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            else:
                if not stack:
                    mark[i] = 1
                else:
                    stack.pop()
        while stack:
            mark[stack[-1]] = 1
            stack.pop()
        ans = length = 0
        for m in mark:
            if m:
                length = 0
            else:
                length += 1
                ans = max(ans, length)
        return ans
