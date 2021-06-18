import math

# 官方题解：数学
class Solution:
    def smallestGoodBase(self, n: str) -> str:
        n = int(n)
        m_max = int(math.log(n, 2))
        for m in range(m_max, 1, -1):
            k = int(pow(n, 1 / m))
            s = (1 - pow(k, m + 1)) // (1 - k)
            if s == n:
                return str(k)
        return str(n - 1)
