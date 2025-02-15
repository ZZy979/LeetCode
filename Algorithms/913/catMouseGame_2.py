# 官方题解2：拓扑排序
# 时间复杂度O(n³)，空间复杂度O(n²)

MOUSE_TURN = 0
CAT_TURN = 1

DRAW = 0
MOUSE_WIN = 1
CAT_WIN = 2

class Solution:
    def catMouseGame(self, graph: List[List[int]]) -> int:
        n = len(graph)
        degrees = [[[0, 0] for _ in range(n)] for _ in range(n)]
        results = [[[0, 0] for _ in range(n)] for _ in range(n)]
        for i in range(n):
            for j in range(1, n):
                degrees[i][j][MOUSE_TURN] = len(graph[i])
                degrees[i][j][CAT_TURN] = len(graph[j])
        for y in graph[0]:
            for i in range(n):
                degrees[i][y][CAT_TURN] -= 1

        q = deque()
        for j in range(1, n):
            results[0][j][MOUSE_TURN] = MOUSE_WIN
            results[0][j][CAT_TURN] = MOUSE_WIN
            q.append((0, j, MOUSE_TURN))
            q.append((0, j, CAT_TURN))
        for i in range(1, n):
            results[i][i][MOUSE_TURN] = CAT_WIN
            results[i][i][CAT_TURN] = CAT_WIN
            q.append((i, i, MOUSE_TURN))
            q.append((i, i, CAT_TURN))

        while q:
            mouse, cat, turn = q.popleft()
            result = results[mouse][cat][turn]
            if turn == MOUSE_TURN:
                prevStates = [(mouse, prev, CAT_TURN) for prev in graph[cat]]
            else:
                prevStates = [(prev, cat, MOUSE_TURN) for prev in graph[mouse]]
            for prevMouse, prevCat, prevTurn in prevStates:
                if prevCat == 0:
                    continue
                if results[prevMouse][prevCat][prevTurn] == DRAW:
                    canWin = result == MOUSE_WIN and prevTurn == MOUSE_TURN or result == CAT_WIN and prevTurn == CAT_TURN
                    if canWin:
                        results[prevMouse][prevCat][prevTurn] = result
                        q.append((prevMouse, prevCat, prevTurn))
                    else:
                        degrees[prevMouse][prevCat][prevTurn] -= 1
                        if degrees[prevMouse][prevCat][prevTurn] == 0:
                            results[prevMouse][prevCat][prevTurn] = CAT_WIN if prevTurn == MOUSE_TURN else MOUSE_WIN
                            q.append((prevMouse, prevCat, prevTurn))
        return results[1][2][MOUSE_TURN]
