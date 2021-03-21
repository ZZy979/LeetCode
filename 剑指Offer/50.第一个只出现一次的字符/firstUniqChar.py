from collections import Counter

class Solution:
    def firstUniqChar(self, s: str) -> str:
        count = Counter(s)
        for c in s:
            if count[c] == 1:
                return c
        return ' '
