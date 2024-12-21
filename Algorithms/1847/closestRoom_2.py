import bisect

# 评论区解法：二分查找
class Solution:
    def closestRoom(self, rooms: List[List[int]], queries: List[List[int]]) -> List[int]:
        n, k = len(rooms), len(queries)
        index = sorted(range(k), key=lambda i: queries[i][1], reverse=True)
        rooms.sort(key=lambda r: r[1], reverse=True)
        ans = [0] * k
        valid = []
        j = 0
        for i in index:
            preferred, min_size = queries[i]
            while j < n and rooms[j][1] >= min_size:
                bisect.insort(valid, rooms[j][0])
                j += 1
            t = bisect.bisect_left(valid, preferred)
            if not valid:
                ans[i] = -1
            elif t == len(valid) or (t >= 1 and preferred - valid[t - 1] <= valid[t] - preferred):
                ans[i] = valid[t - 1]
            else:
                ans[i] = valid[t]
        return ans
