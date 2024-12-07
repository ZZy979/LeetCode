# 官方题解
class Movement:
    def __init__(self, start_x, start_y, end_x, end_y, dx, dy):
        self.start_x = start_x
        self.start_y = start_y
        self.end_x = end_x
        self.end_y = end_y
        self.dx = dx
        self.dy = dy
        self.cur_x = start_x
        self.cur_y = start_y

    def reset(self):
        self.cur_x = self.start_x
        self.cur_y = self.start_y

    def stopped(self):
        return self.cur_x == self.end_x and self.cur_y == self.end_y

    def advance(self):
        if not self.stopped():
            self.cur_x += self.dx
            self.cur_y += self.dy

    def cross(self, other):
        # 每次判断是否相遇时需要重置 cur
        self.reset()
        other.reset()
        while not self.stopped() or not other.stopped():
            self.advance()
            other.advance()
            if self.cur_x == other.cur_x and self.cur_y == other.cur_y:
                return True
        return False

class Solution:
    def countCombinations(self, pieces: List[str], positions: List[List[int]]) -> int:
        rook_directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        bishop_directions = [[1, 1], [1, -1], [-1, 1], [-1, -1]]
        queen_directions = rook_directions + bishop_directions
        n = len(pieces)
        res = 0
        stack = []

        def check(u):
            for v in range(u):
                if stack[u].cross(stack[v]):
                    return False
            return True

        def dfs(u):
            nonlocal res
            if u == n:
                res += 1
                return
            
            if pieces[u] == "rook":
                directions = rook_directions
            elif pieces[u] == "queen":
                directions = queen_directions
            elif pieces[u] == "bishop":
                directions = bishop_directions

            # 处理第 u 个棋子原地不动的情况
            stack.append(Movement(positions[u][0], positions[u][1], positions[u][0], positions[u][1], 0, 0))
            if check(u):
                dfs(u + 1)
            stack.pop()

            # 枚举第 u 个棋子在所有方向、所有步数的情况
            for dire in directions:
                for step in range(1, 8):
                    x = positions[u][0] + dire[0] * step
                    y = positions[u][1] + dire[1] * step
                    if x < 1 or x > 8 or y < 1 or y > 8:
                        break
                    stack.append(Movement(positions[u][0], positions[u][1], x, y, dire[0], dire[1]))
                    if check(u):
                        dfs(u + 1)
                    stack.pop()

        dfs(0)
        return res
