from collections import deque

# 广度优先搜索，时间复杂度O(n(n-k))，超时
class Solution:
    def minReverseOperations(self, n: int, p: int, banned: List[int], k: int) -> List[int]:
        moves = range(-k + 1, k, 2)
        ans = [-1] * n
        ans[p] = 0
        banned = set(banned)
        q = deque([(p, 1)])
        visited = {p}
        while q:
            i, op = q.popleft()
            for m in moves:
                j = i + m
                if 0 <= j < n and k - 1 <= i + j <= 2 * (n - 1) - (k - 1) and j not in visited and j not in banned:
                    ans[j] = op
                    visited.add(j)
                    q.append((j, op + 1))
        return ans
