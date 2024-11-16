# 暴力法
class Solution:
    def countKConstraintSubstrings(self, s: str, k: int) -> int:
        return sum(not k < s[i:j].count('0') < j - i - k for i in range(len(s)) for j in range(i + 1, len(s) + 1))
