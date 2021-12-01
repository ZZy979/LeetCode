from itertools import accumulate
from operator import xor

# 暴力法，时间复杂度O(n³)
# 3768 ms
class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        n = len(arr)
        cumxor = list(accumulate(arr, xor, initial=0))
        return sum(
            1 for i in range(n) for j in range(i + 1, n) for k in range(j, n)
            if cumxor[i] ^ cumxor[j] == cumxor[j] ^ cumxor[k + 1]
        )
