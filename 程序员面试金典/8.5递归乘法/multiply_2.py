class Solution:
    def multiply(self, A: int, B: int) -> int:
        if A > B:
            A, B = B, A
        return multiply_rec(A, B)


def multiply_rec(a, b):
    if a == 0:
        return 0
    elif a == 1:
        return b
    
    half_a = a >> 1
    half_prod = multiply_rec(half_a, b)
    return half_prod + half_prod if a % 2 == 0 else half_prod + half_prod + b
