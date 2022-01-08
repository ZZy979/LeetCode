class Solution:
    def catMouseGame(self, graph: List[List[int]]) -> int:
        n = len(graph)
        dp = [[[-1] * (2 * n) for _ in range(n)] for _ in range(n)]
        return get_result(graph, dp, 1, 2, 0)


DRAW = 0
MOUSE_WIN = 1
CAT_WIN = 2


def get_result(graph, dp, mouse, cat, turns):
    if turns == 2 * len(graph):
        return DRAW
    res = dp[mouse][cat][turns]
    if res != -1:
        return res
    if mouse == 0:
        res = MOUSE_WIN
    elif cat == mouse:
        res = CAT_WIN
    else:
        res = get_next_result(graph, dp, mouse, cat, turns)
    dp[mouse][cat][turns] = res
    return res


def get_next_result(graph, dp, mouse, cat, turns):
    cur_move = mouse if turns % 2 == 0 else cat
    res = default_res = MOUSE_WIN if cur_move != mouse else CAT_WIN
    for i in graph[cur_move]:
        if cur_move == cat and i == 0:
            continue
        next_mouse = i if cur_move == mouse else mouse
        next_cat = i if cur_move == cat else cat
        next_res = get_result(graph, dp, next_mouse, next_cat, turns + 1)
        if next_res != default_res:
            res = next_res
            if res != DRAW:
                break
    return res
