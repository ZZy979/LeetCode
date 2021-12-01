# 官方题解2：BFS
# 时间复杂度O(n^k)，空间复杂度O(n^k+m)
# 48 ms
class Solution:
    def numWays(self, n: int, relation: List[int], k: int) -> int:
        edges = collections.defaultdict(list)
        for u, v in relation:
            edges[u].append(v)
        steps = 0
        queue = collections.deque([0])
        while queue and steps < k:
            steps += 1
            for i in range(len(queue)):
                queue.extend(edges[queue.popleft()])
        ways = 0
        if steps == k:
            while queue:
                if queue.popleft() == n - 1:
                    ways += 1    
        return ways 
