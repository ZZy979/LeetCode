from collections import Counter

class Solution:
    def countLargestGroup(self, n: int) -> int:
        cnt = Counter(sum(map(int, str(i))) for i in range(1, n + 1))
        m = cnt.most_common(1)[0][1]
        return sum(v == m for v in cnt.values())
