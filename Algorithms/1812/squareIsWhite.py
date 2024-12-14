class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        return (ord(coordinates[0]) - ord('a') + 1) % 2 != int(coordinates[1]) % 2
