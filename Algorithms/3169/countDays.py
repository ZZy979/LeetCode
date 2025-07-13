# 排序+区间合并，时间复杂度O(nlog n)，空间复杂度O(log n)
class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        last_end = 0
        ans = 0
        for start, end in meetings:
            if start > last_end:
                ans += start - last_end - 1
            last_end = max(last_end, end)
        return ans + days - last_end
