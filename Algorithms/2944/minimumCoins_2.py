from collections import deque

# 官方题解方法二：单调队列
# 时间复杂度O(n)，空间复杂度O(n)
class Solution:
    def minimumCoins(self, prices: List[int]) -> int:
        n = len(prices)
        q = deque([[n, 0]])
        for i in range(n - 1, -1, -1):
            while q[-1][0] >= 2 * i + 3:
                q.pop()
            cur = q[-1][1] + prices[i]
            while q[0][1] >= cur:
                q.popleft()
            q.appendleft([i, cur])
        return q[0][1]
