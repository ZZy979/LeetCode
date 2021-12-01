from collections import Counter
from operator import itemgetter

# 散列表+排序，时间复杂度O(nlog n)，空间复杂度O(n)
# 72 ms
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        items = sorted(sorted(Counter(words).items(), key=itemgetter(0)), key=itemgetter(1), reverse=True)
        return [w for w, _ in items[:k]]
