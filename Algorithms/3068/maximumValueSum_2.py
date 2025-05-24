# 官方题解二：树形动态规划，时间复杂度O(n)，空间复杂度O(n)
class Solution:
    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        g = defaultdict(list)
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)

        def dfs(u, fa):
            f0, f1 = 0, float('-inf')
            for v in g[u]:
                if v != fa:
                    r0, r1 = dfs(v, u)
                    t = max(f1 + r0, f0 + r1)
                    f0 = max(f0 + r0, f1 + r1)
                    f1 = t
            return (
                max(f0 + nums[u], f1 + (nums[u] ^ k)),
                max(f1 + nums[u], f0 + (nums[u] ^ k))
            )

        return dfs(0, -1)[0]
