class Solution:
    def fairCandySwap(self, A: List[int], B: List[int]) -> List[int]:
        sum_a, sum_b = sum(A), sum(B)
        d = (sum_a - sum_b) // 2
        B = set(B)
        for x in A:
            if x - d in B:
                return [x, x - d]
