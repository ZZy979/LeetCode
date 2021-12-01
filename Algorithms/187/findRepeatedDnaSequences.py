from collections import Counter

class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        if len(s) <= 10:
            return []
        c = Counter(s[i:i + 10] for i in range(len(s) - 9))
        return [k for k, v in c.items() if v > 1]
