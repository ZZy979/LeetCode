class Solution:
    def catMouseGame(self, graph: List[List[int]]) -> int:
        DRAW = 0
        MOUSE_WIN = 1
        CAT_WIN = 2

        @lru_cache(None)
        def dfs(mouse, cat, turns):
            if turns == 2 * len(graph):
                return DRAW
            if mouse == 0:
                return MOUSE_WIN
            elif cat == mouse:
                return CAT_WIN
            if turns % 2 == 0:
                ans = CAT_WIN
                for i in graph[mouse]:
                    if (ret := dfs(i, cat, turns + 1)) == MOUSE_WIN:
                        return MOUSE_WIN
                    elif ret == DRAW:
                        ans = DRAW
                return ans
            else:
                ans = MOUSE_WIN
                for i in graph[cat]:
                    if i == 0:
                        continue
                    if (ret := dfs(mouse, i, turns + 1)) == CAT_WIN:
                        return CAT_WIN
                    elif ret == DRAW:
                        ans = DRAW
                return ans

        return dfs(1, 2, 0)
