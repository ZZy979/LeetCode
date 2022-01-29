from collections import Counter

class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        c = Counter((s1 + ' ' + s2).split())
        return [w for w in c if c[w] == 1]
