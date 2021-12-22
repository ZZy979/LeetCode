class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        indegrees, out_degrees = [0] * (n + 1), [0] * (n + 1)
        for a, b in trust:
            indegrees[b] += 1
            out_degrees[a] += 1
        for i in range(1, n + 1):
            if indegrees[i] == n - 1 and out_degrees[i] == 0:
                return i
        return -1
