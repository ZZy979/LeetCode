class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        incr = decr = True
        for i in range(1, len(A)):
            if A[i] < A[i - 1]:
                incr = False
            elif A[i] > A[i - 1]:
                decr = False
        return incr or decr
