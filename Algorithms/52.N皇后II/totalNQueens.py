class Solution:
    def totalNQueens(self, n: int) -> int:
        if n == 0:
            return 0
        return sum(self.queens(n, []))

    def queens(self, n, state):
        for x in range(n):
            if not self.conflict(state, x):
                state.append(x)
                if len(state) == n:
                    yield 1
                else:
                    for result in self.queens(n, state):
                        yield 1
                state.pop()

    def conflict(self, state, next_x):
        next_y = len(state)
        for y in range(len(state)):
            if abs(state[y] - next_x) in (0, next_y - y):
                return True
        return False
