class NeighborSum:

    def __init__(self, grid: List[List[int]]):
        self.grid = grid
        self.index = {grid[i][j]: (i, j) for i in range(len(grid)) for j in range(len(grid[i]))}

    def adjacentSum(self, value: int) -> int:
        i, j = self.index[value]
        return self.get(i - 1, j) + self.get(i + 1, j) + self.get(i, j - 1) + self.get(i, j + 1)

    def diagonalSum(self, value: int) -> int:
        i, j = self.index[value]
        return self.get(i - 1, j - 1) + self.get(i - 1, j + 1) + self.get(i + 1, j - 1) + self.get(i + 1, j + 1)
    
    def get(self, i, j):
        return self.grid[i][j] if 0 <= i < len(self.grid) and 0 <= j < len(self.grid[i]) else 0


# Your NeighborSum object will be instantiated and called as such:
# obj = NeighborSum(grid)
# param_1 = obj.adjacentSum(value)
# param_2 = obj.diagonalSum(value)
