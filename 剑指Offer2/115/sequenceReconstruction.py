from collections import defaultdict, deque

class Solution:
    def sequenceReconstruction(self, org: List[int], seqs: List[List[int]]) -> bool:
        if not seqs:
            return False
        n = len(org)
        edges = defaultdict(list)
        indegrees = [0] * (n + 1)
        for seq in seqs:
            if not 1 <= seq[0] <= n:
                return False
            for i in range(len(seq) - 1):
                if not 1 <= seq[i + 1] <= n:
                    return False
                edges[seq[i]].append(seq[i + 1])
                indegrees[seq[i + 1]] += 1
        
        q = deque(i for i in range(1, n + 1) if indegrees[i] == 0)
        idx = 0
        while q:
            i = q.popleft()
            if q or org[idx] != i:
                return False
            idx += 1
            for j in edges[i]:
                indegrees[j] -= 1
                if indegrees[j] == 0:
                    q.append(j)
        return idx == n
