# 官方题解2：枚举山脚，64 ms
class Solution:
    def longestMountain(self, A: List[int]) -> int:
        n = len(A)
        ans = left = 0
        while left + 2 < n:
            right = left + 1
            if A[left] < A[left + 1]:
                while right + 1 < n and A[right] < A[right + 1]:
                    right += 1
                if right < n - 1 and A[right] > A[right + 1]:
                    while right + 1 < n and A[right] > A[right + 1]:
                        right += 1
                    ans = max(ans, right - left + 1)
                else:
                    right += 1
            left = right
        return ans
