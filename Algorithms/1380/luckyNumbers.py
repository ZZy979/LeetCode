class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        row_min = {min(row) for row in matrix}
        col_max = {max(col) for col in zip(*matrix)}
        return list(row_min & col_max)
