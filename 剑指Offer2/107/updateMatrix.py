from collections import deque

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        ans = [[0] * n for _ in range(m)]
        q = deque((i, j) for i in range(m) for j in range(n) if mat[i][j] == 0)
        seen = set(q)

        while q:
            i, j = q.popleft()
            for ni, nj in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
                if 0 <= ni < m and 0 <= nj < n and (ni, nj) not in seen:
                    ans[ni][nj] = ans[i][j] + 1
                    q.append((ni, nj))
                    seen.add((ni, nj))
        return ans
