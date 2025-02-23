import bisect

# 官方题解：二分查找
class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        n = len(arr)
        span = n // 4 + 1
        for i in range(0, n, span):
            if bisect.bisect_right(arr, arr[i]) - bisect.bisect_left(arr, arr[i]) >= span:
                return arr[i]
        return -1
