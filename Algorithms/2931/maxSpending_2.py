import itertools

class Solution:
    def maxSpending(self, values: List[List[int]]) -> int:
        return sum(i * v for i, v in enumerate(sorted(itertools.chain.from_iterable(values)), start=1))
