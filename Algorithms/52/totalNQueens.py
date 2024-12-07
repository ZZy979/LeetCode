class Solution:
    def totalNQueens(self, n: int) -> int:
        if n == 0:
            return 0
        self.ans = 0
        self.queens(n, [])
        return self.ans

    def queens(self, n, state):
        for x in range(n):
            if not self.conflict(state, x):
                state.append(x)
                if len(state) == n:
                    self.ans += 1
                else:
                    self.queens(n, state)
                state.pop()

    def conflict(self, state, next_x):
        next_y = len(state)
        for y in range(len(state)):
            if abs(state[y] - next_x) in (0, next_y - y):
                return True
        return False
