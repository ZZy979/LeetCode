from math import ceil, sqrt

# 官方题解：数学
# x+(x-1)+...+1 = x(x+1)/2 >= n
class Solution:
    def twoEggDrop(self, n: int) -> int:
        return ceil((-1 + sqrt(1 + 8 * n)) / 2)
