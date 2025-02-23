import bisect

class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        n = len(arr)
        candidates = {arr[i] for i in (0, n // 4, n // 2, n * 3 // 4, n - 1)}
        count = lambda x: bisect.bisect_right(arr, x) - bisect.bisect_left(arr, x)
        return max(candidates, key=count)
