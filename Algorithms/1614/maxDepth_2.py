class Solution:
    def maxDepth(self, s: str) -> int:
        depth = ans = 0
        for c in s:
            if c == '(':
                depth += 1
                ans = max(ans, depth)
            elif c == ')':
                depth -= 1
        return ans
