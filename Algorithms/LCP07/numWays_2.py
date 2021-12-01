# 官方题解1：DFS
# 时间复杂度O(n^k)，空间复杂度O(n+m+k)
# 40 ms
class Solution:
    def numWays(self, n: int, relation: List[int], k: int) -> int:
        self.ways, self.n, self.k = 0, n, k
        self.edges = collections.defaultdict(list)
        for src, dst in relation:
            self.edges[src].append(dst)
        self.dfs(0, 0)
        return self.ways 

    def dfs(self, index, steps):
        if steps == self.k:
            if index == self.n - 1:
                self.ways += 1
            return
        for to in self.edges[index]:
            self.dfs(to, steps + 1)
