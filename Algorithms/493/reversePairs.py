import bisect
from collections import defaultdict

# 暴力法，超时。。
class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        num_idx = defaultdict(list)
        for i, x in enumerate(nums):
            bisect.insort(num_idx[x], i)
        keys = list(sorted(num_idx))

        ans = 0
        for ki in keys:
            for kj in keys[:bisect.bisect_left(keys, ki / 2)]:
                for idx in num_idx[ki]:
                    ans += len(num_idx[kj]) - bisect.bisect(num_idx[kj], idx)
        return ans
