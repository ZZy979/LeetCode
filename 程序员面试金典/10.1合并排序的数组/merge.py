class Solution:
    def merge(self, A: List[int], m: int, B: List[int], n: int) -> None:
        """
        Do not return anything, modify A in-place instead.
        """
        p = len(A) - 1
        m -= 1
        n -= 1
        while m >= 0 and n >= 0:
            if B[n] >= A[m]:
                A[p] = B[n]
                n -= 1
            else:
                A[p] = A[m]
                m -= 1
            p -= 1
        while n >= 0:
            A[p] = B[n]
            n -= 1
            p -= 1
