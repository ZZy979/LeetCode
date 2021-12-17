class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        dp0 = dp1 = 0
        for c in s:
            dp0, dp1 = dp0 + int(c), min(dp0, dp1) + 1 - int(c)
        return min(dp0, dp1)
