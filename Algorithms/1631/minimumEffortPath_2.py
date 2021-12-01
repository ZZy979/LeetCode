# 官方题解1：二分查找+BFS
# 时间复杂度O(mnlog C)（C是格子的最大高度），空间复杂度O(mn)
# 3348 ms
class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        m, n = len(heights), len(heights[0])
        left, right, ans = 0, 10**6 - 1, 0
        while left <= right:
            mid = (left + right) // 2
            q = collections.deque([(0, 0)])
            seen = {(0, 0)}
            while q:
                x, y = q.popleft()
                for nx, ny in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
                    if 0 <= nx < m and 0 <= ny < n and (nx, ny) not in seen and abs(heights[x][y] - heights[nx][ny]) <= mid:
                        q.append((nx, ny))
                        seen.add((nx, ny))
            if (m - 1, n - 1) in seen:
                ans = mid
                right = mid - 1
            else:
                left = mid + 1
        return ans
