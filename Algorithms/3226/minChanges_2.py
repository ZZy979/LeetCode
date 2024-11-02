# 官方题解：位运算
class Solution:
    def minChanges(self, n: int, k: int) -> int:
        return (n ^ k).bit_count() if n & k == k else -1
