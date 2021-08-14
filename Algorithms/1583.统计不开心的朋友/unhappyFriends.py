class Solution:
    def unhappyFriends(self, n: int, preferences: List[List[int]], pairs: List[List[int]]) -> int:
        rank = []
        for i, p in enumerate(preferences):
            r = [0] * n
            for j in range(n - 1):
                r[p[j]] = j
            rank.append(r)
        partner = [0] * n
        for x, y in pairs:
            partner[x] = y
            partner[y] = x
        return sum(
            1 for x in range(n)
            if any(rank[u][x] < rank[u][partner[u]] for u in preferences[x][:rank[x][partner[x]]])
        )
