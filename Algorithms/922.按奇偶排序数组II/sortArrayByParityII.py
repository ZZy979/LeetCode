# 268 ms
class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        even, odd = 0, 1
        while even < len(A) and odd < len(A):
            while even < len(A) and A[even] % 2 == 0:
                even += 2
            while odd < len(A) and A[odd] % 2 == 1:
                odd += 2
            if even < len(A) and odd < len(A):
                A[even], A[odd] = A[odd], A[even]
                even += 2
                odd += 2
        return A
