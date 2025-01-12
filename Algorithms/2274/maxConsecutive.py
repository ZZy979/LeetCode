class Solution:
    def maxConsecutive(self, bottom: int, top: int, special: List[int]) -> int:
        special.extend([bottom - 1, top + 1])
        special.sort()
        return max(special[i] - special[i - 1] - 1 for i in range(1, len(special)))
