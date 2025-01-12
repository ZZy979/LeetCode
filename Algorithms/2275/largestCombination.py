class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        return max(sum((x & (1 << i)) != 0 for x in candidates) for i in range(24))
