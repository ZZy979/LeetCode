# 官方题解：差分数组
class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        diff = [0] * 52
        for l, r in ranges:
            diff[l] += 1
            diff[r + 1] -= 1
        curr = 0
        for i in range(1, 51):
            curr += diff[i]
            if left <= i <= right and curr <= 0:
                return False
        return True
