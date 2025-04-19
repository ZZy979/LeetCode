# 暴力法，时间复杂度O(n³)，空间复杂度O(1)
class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        n = len(arr)
        return sum(
            abs(arr[i] - arr[j]) <= a and abs(arr[j] - arr[k]) <= b and abs(arr[i] - arr[k]) <= c
            for i in range(n - 2) for j in range(i + 1, n - 1) for k in range(j + 1, n))
