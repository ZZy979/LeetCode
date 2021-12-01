class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]
        start, start_contains = find(intervals, newInterval[0])
        end, end_contains = find(intervals, newInterval[1])
        if start == end:
            if not start_contains and not end_contains:
                # 包含start == -1的情况
                intervals.insert(start + 1, newInterval)
            elif not start_contains and end_contains:
                intervals[start][0] = newInterval[0]
            elif start_contains and not end_contains:
                intervals[start][1] = newInterval[1]
        else:
            # start == -1 -> 修改intervals[0][0]
            if not start_contains:
                start += 1
            intervals[start:end + 1] = [[min(intervals[start][0], newInterval[0]), max(intervals[end][1], newInterval[1])]]
        return intervals


def find(intervals, num):
    '''
    返回(i, c)，如果i == -1则c == False, num在intervals[0]之前；
    如果i >= 0，如果c为True则intervals[i]包含num，否则num在intervals[i]和intervals[i + 1]之间
    '''
    i = 0
    while i < len(intervals):
        if num < intervals[i][0]:
            break
        i += 1
    i -= 1
    return i, intervals[i][0] <= num <= intervals[i][1]
