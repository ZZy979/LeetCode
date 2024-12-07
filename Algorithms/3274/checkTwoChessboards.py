class Solution:
    def checkTwoChessboards(self, coordinate1: str, coordinate2: str) -> bool:
        x1, y1 = ord(coordinate1[0]) - ord('a') + 1, int(coordinate1[1])
        x2, y2 = ord(coordinate2[0]) - ord('a') + 1, int(coordinate2[1])
        return (x1 % 2 == y1 % 2) == (x2 % 2 == y2 % 2)
