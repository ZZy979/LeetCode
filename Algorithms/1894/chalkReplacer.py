import bisect
from itertools import accumulate

class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        presum = list(accumulate(chalk))
        return bisect.bisect_right(presum, k % presum[-1])
