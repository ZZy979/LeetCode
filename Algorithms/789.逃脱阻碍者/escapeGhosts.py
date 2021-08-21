class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        xt, yt = target
        return not any(abs(x - xt) + abs(y - yt) <= abs(xt) + abs(yt) for x, y in ghosts)
