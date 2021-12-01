class Solution:
    def multiply(self, A: int, B: int) -> int:
        if A < B:
            A, B = B, A
        return A if B == 1 else A + self.multiply(A, B - 1)
