import math
from collections import Counter

class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        if n <= 2:
            return n
        ans = 0
        for i in range(n):
            if ans >= n - i or ans > n // 2:
                return ans
            count = Counter(calc_slope(points[i], points[j]) for j in range(i + 1, n))
            ans = max(ans, count.most_common(1)[0][1] + 1)
        return ans


def calc_slope(p1, p2):
    dx = p1[0] - p2[0]
    dy = p1[1] - p2[1]
    if dx == 0:
        dy = 1
    elif dy == 0:
        dx = 1
    else:
        if dy < 0:
            dx, dy = -dx, -dy
        g = math.gcd(abs(dx), abs(dy))
        dx //= g
        dy //= g
    return dy + dx * 20001
