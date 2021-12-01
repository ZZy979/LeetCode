class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        return sorted(x**2 for x in A)
