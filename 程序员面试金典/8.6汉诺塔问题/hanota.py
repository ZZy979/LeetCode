class Solution:
    def hanota(self, A: List[int], B: List[int], C: List[int]) -> None:
        """
        Do not return anything, modify C in-place instead.
        """
        self.hanoi(A, B, C, len(A))
    
    def hanoi(self, A, B, C, n):
        if n == 1:
            C.append(A.pop())
        else:
            self.hanoi(A, C, B, n - 1)
            C.append(A.pop())
            self.hanoi(B, A, C, n - 1)
