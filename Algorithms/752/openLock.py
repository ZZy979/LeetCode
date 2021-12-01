from collections import deque

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if target == '0000':
            return 0
        deadends = set(deadends)
        if '0000' in deadends:
            return -1
        q = deque([('0000', 0)])
        visited = {'0000'}
        while q:
            v, n = q.popleft()
            for u in adj(v):
                if u not in deadends and u not in visited:
                    if u == target:
                        return n + 1
                    q.append((u, n + 1))
                    visited.add(u)
        return -1


def adj(v):
    v = list(map(int, v))
    for i in range(4):
        x = v[i]
        v[i] = (x + 1) % 10
        yield ''.join(map(str, v))
        v[i] = (x - 1) % 10
        yield ''.join(map(str, v))
        v[i] = x
