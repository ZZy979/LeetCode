# 官方题解：基于二分查找的动态规划，时间复杂度O(nlog n)
# 180 ms
class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        if not envelopes:
            return 0
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        f = [envelopes[0][1]]
        for i in range(1, len(envelopes)):
            if (num := envelopes[i][1]) > f[-1]:
                f.append(num)
            else:
                index = bisect.bisect_left(f, num)
                f[index] = num
        return len(f)
