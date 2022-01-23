from collections import defaultdict, deque

class Solution:
    def minJumps(self, arr: List[int]) -> int:
        idx = defaultdict(list)
        for i, x in enumerate(arr):
            idx[x].append(i)

        n = len(arr)
        q = deque([(0, 0)])
        visited = {0}
        while q:
            i, step = q.popleft()
            if i == n - 1:
                return step
            for j in idx[arr[i]]:
                if j not in visited:
                    visited.add(j)
                    q.append((j, step + 1))
            del idx[arr[i]]  # 注意删除子图，避免超时

            if i < n - 1 and i + 1 not in visited:
                visited.add(i + 1)
                q.append((i + 1, step + 1))
            if i > 0 and i - 1 not in visited:
                visited.add(i - 1)
                q.append((i - 1, step + 1))
        return step
