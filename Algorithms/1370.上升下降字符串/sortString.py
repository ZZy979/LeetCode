from collections import Counter

class Solution:
    def sortString(self, s: str) -> str:
        count = Counter(s)
        sorted_letters = list(sorted(count))
        res = []
        n = len(s)
        while n:
            for k in sorted_letters:
                if count[k]:
                    res.append(k)
                    count[k] -= 1
                    n -= 1
            for k in reversed(sorted_letters):
                if count[k]:
                    res.append(k)
                    count[k] -= 1
                    n -= 1
        return ''.join(res)
