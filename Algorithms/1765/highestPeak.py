from collections import deque

class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        m, n = len(isWater), len(isWater[0])
        height = [[-1] * n for _ in range(m)]

        q = deque()
        for i in range(m):
            for j in range(n):
                if isWater[i][j]:
                    height[i][j] = 0
                    q.append((i, j))
        while q:
            i, j = q.popleft()
            for ni, nj in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
                if 0 <= ni < m and 0 <= nj < n and height[ni][nj] == -1:
                    height[ni][nj] = height[i][j] + 1
                    q.append((ni, nj))
        return height
