from collections import Counter
from functools import reduce

# 一行版本
class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        return list(reduce(lambda x, y: x & y, map(Counter, A)).elements())
