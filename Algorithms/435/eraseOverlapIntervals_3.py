# 评论区解法
# 时间复杂度O(nlog n)
# 76 ms
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        cnt = 0
        pre = 0
        for i in range(1, len(intervals)):
            if intervals[i][0] < intervals[pre][1]:
                if intervals[pre][1] > intervals[i][1]:
                    pre = i
                cnt +=1
            else:
                pre = i
        return cnt
