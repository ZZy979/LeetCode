class Solution:
    def movingCount(self, m: int, n: int, k: int) -> int:
        visited = [[False] * n for _ in range(m)]
        self.ans = 0
        self.dfs(m, n, k, visited, 0, 0)
        return self.ans
    
    def dfs(self, m, n, k, visited, r, c):
        visited[r][c] = True
        self.ans += 1
        for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            nr, nc = r + dr, c + dc
            if 0 <= nr < m and 0 <= nc < n and not visited[nr][nc] and digit_sum(nr) + digit_sum(nc) <= k:
                self.dfs(m, n, k, visited, nr, nc)


def digit_sum(x):
    s = 0
    while x:
        s += x % 10
        x //= 10
    return s
