from collections import Counter

class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        c1, c2 = Counter(s1.split()), Counter(s2.split())
        return [w for w in c1 if c1[w] == 1 and w not in c2] + [w for w in c2 if c2[w] == 1 and w not in c1]
