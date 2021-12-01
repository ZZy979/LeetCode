from functools import reduce
from operator import xor

class Solution:
    def decode(self, encoded: List[int]) -> List[int]:
        n = len(encoded) + 1
        start = reduce(xor, range(1, n + 1)) ^ reduce(xor, encoded[1::2])
        perm = [start]
        for x in encoded:
            perm.append(perm[-1] ^ x)
        return perm
