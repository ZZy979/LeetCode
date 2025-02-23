import bisect
from collections import defaultdict

class RangeFreqQuery:

    def __init__(self, arr: List[int]):
        self.index_map = defaultdict(list)
        for i, x in enumerate(arr):
            self.index_map[x].append(i)

    def query(self, left: int, right: int, value: int) -> int:
        idx = self.index_map[value]
        return bisect.bisect_right(idx, right) - bisect.bisect_left(idx, left)


# Your RangeFreqQuery object will be instantiated and called as such:
# obj = RangeFreqQuery(arr)
# param_1 = obj.query(left,right,value)
