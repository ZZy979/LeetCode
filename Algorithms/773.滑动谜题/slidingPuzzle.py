from collections import deque

class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        start = ''.join(map(str, board[0])) + ''.join(map(str, board[1]))
        target = '123450'
        q = deque([(start, 0)])
        visited = set()
        while q:
            v, n = q.popleft()
            visited.add(v)
            if v == target:
                return n
            for u in adj(v):
                if u not in visited:
                    q.append((u, n + 1))
        return -1


def idx(r, c):
    return r * 3 + c


def adj(v):
    b = list(v)
    r, c = divmod(b.index('0'), 3)
    b[idx(r, c)], b[idx((r + 1) % 2, c)] = b[idx((r + 1) % 2, c)], b[idx(r, c)]
    yield ''.join(b)
    b[idx(r, c)], b[idx((r + 1) % 2, c)] = b[idx((r + 1) % 2, c)], b[idx(r, c)]
    if c > 0:
        b[idx(r, c)], b[idx(r, c - 1)] = b[idx(r, c - 1)], b[idx(r, c)]
        yield ''.join(b)
        b[idx(r, c)], b[idx(r, c - 1)] = b[idx(r, c - 1)], b[idx(r, c)]
    if c < 2:
        b[idx(r, c)], b[idx(r, c + 1)] = b[idx(r, c + 1)], b[idx(r, c)]
        yield ''.join(b)
        b[idx(r, c)], b[idx(r, c + 1)] = b[idx(r, c + 1)], b[idx(r, c)]
