from collections import Counter
from itertools import combinations

# 评论区解法
class Solution:
    def findNumOfValidWords(self, words: List[str], puzzles: List[str]) -> List[int]:
        counter = Counter(filter(lambda x: len(x) <= 7, map(frozenset, words)))
        return [
            sum(sum(counter[frozenset((p[0],) + comb)] for comb in combinations(p[1:], r)) for r in range(7))
            for p in puzzles
        ]
