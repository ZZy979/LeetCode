class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        if n == 0:
            return [[]]
        return [
            ['.' * p + 'Q' + '.' * (n - p - 1) for p in result]
            for result in self.queens(n, ())
        ]
    
    def queens(self, n, state):
        for x in range(n):
            if not self.conflict(state, x):
                if len(state) == n - 1:
                    yield (x,)
                else:
                    for result in self.queens(n, state + (x,)):
                        yield (x,) + result
    
    def conflict(self, state, next_x):
        next_y = len(state)
        for y in range(next_y):
            if abs(state[y] - next_x) in (0, next_y - y):
                return True
        return False
