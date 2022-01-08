class Solution:
    def maxDepth(self, s: str) -> int:
        stack = [0]
        for c in s:
            if c == '(':
                stack.append(c)
            elif c == ')':
                depth = 0
                while stack[-1] != '(':
                    depth = max(depth, stack.pop())
                stack[-1] = depth + 1
        return max(stack)
