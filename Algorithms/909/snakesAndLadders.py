class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)

        def id2rc(idx: int) -> (int, int):
            r, c = (idx - 1) // n, (idx - 1) % n
            if r % 2 == 1:
                c = n - 1 - c
            return n - 1 - r, c
        
        visited = set()
        q = deque([(1, 0)])
        while q:
            idx, step = q.popleft()
            for i in range(1, 7):
                idx_nxt = idx + i
                if idx_nxt > n * n:
                    break
                x_nxt, y_nxt = id2rc(idx_nxt)
                if board[x_nxt][y_nxt] > 0:
                    idx_nxt = board[x_nxt][y_nxt]
                if idx_nxt == n * n:
                    return step + 1
                if idx_nxt not in visited:
                    visited.add(idx_nxt)
                    q.append((idx_nxt, step + 1))
        return -1
