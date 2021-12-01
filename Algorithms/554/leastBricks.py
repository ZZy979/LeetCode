from collections import Counter

class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        n = len(wall)
        edges = Counter()
        for row in wall:
            s = 0
            for c in range(len(row) - 1):
                s += row[c]
                edges[s] += 1
        return n - edges.most_common(1)[0][1] if edges else n
