# 官方题解：组合数学（隔板+容斥），时间复杂度O(1)
class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        return c(n + 2) - 3 * c(n - (limit + 1) + 2) + 3 * c(n - 2 * (limit + 1) + 2) - c(n - 3 * (limit + 1) + 2)

# 计算C(n, 2)
def c(n):
    return 0 if n <= 0 else n * (n - 1) // 2
