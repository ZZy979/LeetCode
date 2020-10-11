from collections import Counter

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        mchars = Counter(magazine)
        for c in ransomNote:
            if mchars.get(c, 0) == 0:
                return False
            else:
                mchars[c] -= 1
        return True
