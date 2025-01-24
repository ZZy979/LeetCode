from functools import cache

# 官方题解：记忆化搜索
# 时间复杂度O(nC)，空间复杂度O(nC)，其中C=14
class Solution:
    def maximumPoints(self, edges: List[List[int]], coins: List[int], k: int) -> int:
        n = len(coins)
        children = [[] for _ in range(n)]
        for u, v in edges:
            children[u].append(v)
            children[v].append(u)
        
        @cache
        def dfs(node, parent, t):
            """祖先总共做了t次除二操作，以node为根节点的子树可以获得的最大积分"""
            res0 = (coins[node] >> t) - k
            res1 = coins[node] >> (t + 1)
            for child in children[node]:
                if child == parent:
                    continue
                res0 += dfs(child, node, t)
                if t + 1 < 14:
                    res1 += dfs(child, node, t + 1)
            return max(res0, res1)
        
        return dfs(0, -1, 0)
