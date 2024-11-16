# 位运算
class Solution:
    def countKConstraintSubstrings(self, s: str, k: int) -> int:
        x = int(s, 2)
        n = len(s)
        return sum(not k < (x & (((1 << (j - i)) - 1) << i)).bit_count() < j - i - k for i in range(n) for j in range(i + 1, n + 1))
