# 官方题解2：广度优先搜索，时间复杂度O(n²)，空间复杂度O(n)
# 148 ms
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        visited = set()
        circles = 0
        for i in range(n):
            if i not in visited:
                q = collections.deque([i])
                while q:
                    j = q.popleft()
                    visited.add(j)
                    for k in range(n):
                        if isConnected[j][k] == 1 and k not in visited:
                            q.append(k)
                circles += 1
        return circles
