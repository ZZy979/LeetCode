import re
from collections import Counter

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        c = Counter(re.split(r'\W+', paragraph.lower()))
        banned = set(banned)
        return next(w for w, _ in c.most_common() if w not in banned)
