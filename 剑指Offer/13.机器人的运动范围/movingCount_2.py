class Solution:
    def movingCount(self, m: int, n: int, k: int) -> int:
        q = [(0, 0)]
        visited = set()
        while q:
            r, c = q.pop()
            visited.add((r, c))
            for dr, dc in ((0, 1), (1, 0)):
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and (nr, nc) not in visited and digit_sum(nr) + digit_sum(nc) <= k:
                    q.append((nr, nc))
        return len(visited)


def digit_sum(x):
    # x < 100
    return x // 10 + x % 10
