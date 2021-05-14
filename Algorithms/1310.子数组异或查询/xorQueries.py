from itertools import accumulate
from operator import xor

class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        cumxor = list(accumulate(arr, xor, initial=0))
        return [cumxor[l] ^ cumxor[r + 1] for l, r in queries]
