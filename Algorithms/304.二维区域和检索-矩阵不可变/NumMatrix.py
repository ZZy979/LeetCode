from itertools import accumulate

class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.cumsum = [list(accumulate(row, initial=0)) for row in matrix]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return sum(self.cumsum[r][col2 + 1] - self.cumsum[r][col1] for r in range(row1, row2 + 1))


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
