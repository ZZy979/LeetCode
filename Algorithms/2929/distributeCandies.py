# 枚举，时间复杂度O(min(limit, n))
class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        return sum(max(min(limit, n - i) - max(0, n - i - limit) + 1, 0) for i in range(min(n, limit) + 1))
