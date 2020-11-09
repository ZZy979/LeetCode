import heapq
import math

class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        distances = [(math.sqrt(x**2 + y**2), i) for i, (x, y) in enumerate(points)]
        return [points[i] for d, i in heapq.nsmallest(K, distances)]
