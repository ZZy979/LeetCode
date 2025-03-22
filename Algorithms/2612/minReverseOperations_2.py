from collections import deque
from sortedcontainers import SortedList

# 官方题解：广度优先搜索+有序集合（避免重复检查）
# 时间复杂度O(nlog n)，空间复杂度O(n)
class Solution:
    def minReverseOperations(self, n: int, p: int, banned: List[int], k: int) -> List[int]:
        banned = set(banned)
        unreached = [SortedList(), SortedList()]  # 尚未到达的偶数和奇数下标
        for i in range(n):
            if i != p and i not in banned:
                unreached[i % 2].add(i)
        ans = [-1] * n
        ans[p] = 0
        q = deque([p])
        while q:
            i = q.popleft()
            mn = max(i - k + 1, k - i - 1)
            mx = min(i + k - 1, 2 * n - k - i - 1)
            s = unreached[mx % 2]
            visited = []
            for j in s.irange(mn, mx):
                ans[j] = ans[i] + 1
                q.append(j)
                visited.append(j)
            for j in visited:
                s.remove(j)
        return ans
