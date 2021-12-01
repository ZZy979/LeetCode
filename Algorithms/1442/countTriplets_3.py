from collections import Counter
from itertools import accumulate
from operator import xor

# 官方题解2：哈希表，时间复杂度O(n)
# 52 ms
class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        n = len(arr)
        cumxor = list(accumulate(arr, xor, initial=0))
        cnt, total = Counter(), Counter()
        ans = 0
        for k in range(n):
            if cumxor[k + 1] in cnt:
                ans += cnt[cumxor[k + 1]] * k - total[cumxor[k + 1]]
            cnt[cumxor[k]] += 1
            total[cumxor[k]] += k
        return ans
