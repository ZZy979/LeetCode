class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        indegrees = Counter(b for _, b in trust)
        outdegrees = Counter(a for a, _ in trust)
        return next((i for i in range(1, n + 1) if indegrees[i] == n - 1 and outdegrees[i] == 0), -1)
