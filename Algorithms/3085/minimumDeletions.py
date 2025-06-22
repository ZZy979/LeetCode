import bisect
from collections import Counter
from itertools import accumulate

# 散列表+前缀和+二分查找，时间复杂度O(n+Clog C)，空间复杂度O(C)，其中C=26
class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        cnt = sorted(Counter(word).values())
        n = len(cnt)
        prefix_sum = list(accumulate(cnt, initial=0))
        ans = float('inf')
        for i, c in enumerate(cnt):
            # 删除cnt[i]之前的所有字符，cnt[j..n]全部变为c+k
            j = bisect.bisect_right(cnt, c + k)
            ans = min(ans, prefix_sum[i] + prefix_sum[-1] - prefix_sum[j] - (n - j) * (c + k))
        return ans
