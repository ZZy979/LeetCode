from collections import defaultdict
from functools import reduce

# 官方题解：字典树
class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        words = list(set(words))
        Trie = lambda: defaultdict(Trie)
        trie = Trie()
        nodes = [reduce(defaultdict.__getitem__, word[::-1], trie) for word in words]
        return sum(len(word) + 1 for i, word in enumerate(words) if len(nodes[i]) == 0)
