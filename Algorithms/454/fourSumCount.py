from collections import Counter

class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        sum_count_ab = Counter(a + b for a in A for b in B)
        return sum(sum_count_ab[-c - d] for c in C for d in D)
