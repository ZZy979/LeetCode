class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        row = [0] * (rowIndex + 1)
        row[0] = 1
        for i in range(1, rowIndex + 1):
            row[i] = row[i - 1] * (rowIndex - i + 1) // i
        return row
