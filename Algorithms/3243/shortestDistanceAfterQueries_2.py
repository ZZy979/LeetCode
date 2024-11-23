# 方法二：动态规划，时间复杂度O(q(n+q))，空间复杂度O(n+q)
class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        dp = list(range(n))  # dp[i]表示城市0到城市i的最短路径
        prev = [[i - 1] for i in range(n)]  # prev[i]表示通往城市i的所有单向道路的起始城市集合
        prev[0] = []
        res = []
        for u, v in queries:
            prev[v].append(u)
            for i in range(v, n):
                for j in prev[i]:
                    dp[i] = min(dp[i], dp[j] + 1)
            res.append(dp[-1])
        return res
