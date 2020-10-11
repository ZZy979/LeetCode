class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        r1 = [1]
        r2 = [1, 1]
        for i in range(1, rowIndex + 1):
            for j in range(1, i):
                r2[j] = r1[j - 1] + r1[j]
            r1, r2 = r2, [1] * (i + 2)
        return r1
