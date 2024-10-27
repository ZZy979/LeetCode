# 位运算
class Solution:
    def maxTotalReward(self, rewardValues: List[int]) -> int:
        rewardValues.sort()
        f = 1
        for x in rewardValues:
            f |= (f & ((1 << x) - 1)) << x
        return f.bit_length() - 1
