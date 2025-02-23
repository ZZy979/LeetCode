# 官方题解
class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        res = 0
        min_val, max_val = arrays[0][0], arrays[0][-1]
        for arr in arrays[1:]:
            res = max(res, arr[-1] - min_val, max_val - arr[0])
            min_val = min(min_val, arr[0])
            max_val = max(max_val, arr[-1])
        return res
