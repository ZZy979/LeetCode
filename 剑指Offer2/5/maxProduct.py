from functools import reduce
from operator import or_

class Solution:
    def maxProduct(self, words: List[str]) -> int:
        char_bits = [reduce(or_, (1 << (ord(c) - ord('a')) for c in word)) for word in words]
        return max((len(words[i]) * len(words[j]) for i in range(len(words)) for j in range(i + 1, len(words)) if char_bits[i] & char_bits[j] == 0), default=0)
