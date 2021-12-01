# 评论区解法
class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        n = len(arr)
        return sum((((i + 1) // 2) * ((n - i) // 2) + ((i + 2) // 2) * ((n - i + 1) // 2)) * x for i, x in enumerate(arr))
