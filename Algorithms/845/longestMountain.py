# 寻找连续上升+连续下降，100 ms
class Solution:
    def longestMountain(self, A: List[int]) -> int:
        n = len(A)
        if n < 3:
            return 0
        longest = 0
        i = 1
        while i < n:
            while i < n and sign(A, i) != 1:
                i += 1
            mountain_len = 1
            up = down = False
            while i < n and sign(A, i) == 1:
                up = True
                mountain_len += 1
                i += 1
            while i < n and sign(A, i) == -1:
                down = True
                mountain_len += 1
                i += 1
            if up and down:
                longest = max(longest, mountain_len)
        return longest


def sign(A, i):
    return 1 if A[i] > A[i - 1] else -1 if A[i] < A[i - 1] else 0
