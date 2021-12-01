# 方法2：排序+双指针，时间复杂度O(alog a + blog b)
# 200 ms
class Solution:
    def smallestDifference(self, a: List[int], b: List[int]) -> int:
        a.sort()
        b.sort()
        i, j = 0, 0
        min_diff = 0x7fffffff
        while i < len(a) and j < len(b):
            if abs(a[i] - b[j]) < min_diff:
                min_diff = abs(a[i] - b[j])
            if a[i] < b[j]:
                i += 1
            else:
                j += 1
        return min_diff
