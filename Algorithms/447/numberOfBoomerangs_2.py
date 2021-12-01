from collections import Counter

class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        ans = 0
        for xi, yi in points:
            c = Counter((xj - xi) ** 2 + (yj - yi) ** 2 for xj, yj in points)
            ans += sum(m * (m - 1) for m in c.values())
        return ans
