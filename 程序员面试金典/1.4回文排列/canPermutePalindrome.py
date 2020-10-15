from collections import Counter

class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        c = Counter(s)
        return sum(1 for k in c if c[k] % 2 == 1) <= 1
