from collections import Counter

class Solution:
    def CheckPermutation(self, s1: str, s2: str) -> bool:
        return Counter(map(ord, s1)) == Counter(map(ord, s2))
