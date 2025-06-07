# 枚举，时间复杂度O(n²)，空间复杂度O(1)
class Solution:
    def lastSubstring(self, s: str) -> str:
        m = max(s)
        return max(s[i:] for i in range(len(s)) if s[i] == m)
