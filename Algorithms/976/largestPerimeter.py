class Solution:
    def largestPerimeter(self, A: List[int]) -> int:
        A.sort()
        for i in range(len(A) - 3, -1, -1):
            if A[i + 1] - A[i] < A[i + 2] < A[i + 1] + A[i]:
                return A[i] + A[i + 1] + A[i + 2]
        return 0
