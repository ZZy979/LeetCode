class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        n = len(coordinates)
        if coordinates[0][0] == coordinates[1][0]:
            return all(coordinates[i][0] == coordinates[0][0] for i in range(2, n))
        else:
            k = (coordinates[1][1] - coordinates[0][1]) / (coordinates[1][0] - coordinates[0][0])
            b = coordinates[0][1] - k * coordinates[0][0]
            return all(abs(k * coordinates[i][0] + b - coordinates[i][1]) < 1e-2 for i in range(2, n))
