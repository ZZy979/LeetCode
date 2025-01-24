class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        n = len(piles) // 3
        return sum(sorted(piles)[n::2])
