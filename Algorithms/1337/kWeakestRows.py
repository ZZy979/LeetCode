import heapq

class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        weakness = [(mat[r].count(1), r) for r in range(len(mat))]
        return [r for _, r in heapq.nsmallest(k, weakness)]
