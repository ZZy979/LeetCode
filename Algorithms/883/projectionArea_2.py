class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        return sum(v > 0 for row in grid for v in row) + sum(map(max, grid)) + sum(map(max, zip(*grid)))
