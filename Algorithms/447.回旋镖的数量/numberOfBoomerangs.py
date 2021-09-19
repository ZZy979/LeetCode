from collections import Counter

class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        n = len(points)
        if n < 3:
            return 0
        dist_count = [Counter() for _ in range(n)]
        for i in range(n - 1):
            xi, yi = points[i]
            for j in range(i + 1, n):
                xj, yj = points[j]
                d = (xj - xi) ** 2 + (yj - yi) ** 2
                dist_count[i][d] += 1
                dist_count[j][d] += 1
        return sum(m * (m - 1) for c in dist_count for d, m in c.items())
