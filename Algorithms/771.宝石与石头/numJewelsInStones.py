class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        return sum(1 for s in S if s in set(J))
