from collections import Counter

class Solution:
    def frequencySort(self, s: str) -> str:
        c = Counter(s)
        return ''.join(sorted(sorted(s), key=c.__getitem__, reverse=True))
