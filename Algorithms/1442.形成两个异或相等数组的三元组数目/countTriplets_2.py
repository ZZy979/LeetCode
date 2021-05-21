from itertools import accumulate
from operator import xor

# 官方题解：两层循环，时间复杂度O(n²)
# 52 ms
class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        n = len(arr)
        cumxor = list(accumulate(arr, xor, initial=0))
        return sum(
            k - i for i in range(n) for k in range(i + 1, n)
            if cumxor[i] ^ cumxor[k + 1] == 0
        )
