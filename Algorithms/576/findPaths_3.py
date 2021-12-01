import functools

# 评论区解法：DFS+LRU，64 ms
class Solution:
    def findPaths(self, m: int, n: int, N: int, i: int, j: int) -> int:
        @functools.lru_cache(None)
        def dfs(i, j, N):
            if i < 0 or i >= m or j < 0 or j >= n:
                return 1
            if N == 0:
                return 0
            return dfs(i + 1, j, N - 1) + dfs(i - 1, j, N - 1) + dfs(i, j + 1, N - 1) + dfs(i, j - 1, N - 1)

        return dfs(i, j, N) % (10 ** 9 + 7)
