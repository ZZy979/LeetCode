class Solution:
    def balancedStringSplit(self, s: str) -> int:
        d = ans = 0
        for c in s:
            if c == 'L':
                d += 1
            else:
                d -= 1
            if d == 0:
                ans += 1
        return ans
