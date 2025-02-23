from sortedcontainers import SortedDict

class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        left, right = SortedDict(), SortedDict()
        for i, arr in enumerate(arrays):
            left.setdefault(arr[0], []).append(i)
            right.setdefault(arr[-1], []).append(i)
            if len(left) > 2:
                left.popitem()
            if len(right) > 2:
                right.popitem(0)
        d1 = min(right) - min(left) if len(left[min(left)]) == 1 and left[min(left)] == right[max(right)] else max(right) - min(left)
        d2 = max(right) - max(left) if len(right[max(right)]) == 1 and right[max(right)] == left[min(left)] else max(right) - min(left)
        return max(d1, d2)
