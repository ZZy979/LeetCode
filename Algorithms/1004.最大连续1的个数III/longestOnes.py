class Solution:
    def longestOnes(self, A: List[int], K: int) -> int:
        n = len(A)
        n0 = 0
        left = right = 0
        while right < n:
            n0 += A[right] == 0
            if n0 > K:
                n0 -= A[left] == 0
                left += 1
            right += 1
        return right - left
