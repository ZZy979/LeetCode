import heapq

# https://leetcode.cn/problems/maximum-number-of-events-that-can-be-attended/solutions/3707151/liang-chong-fang-fa-zui-xiao-dui-bing-ch-ijbf/
# 最小堆，时间复杂度O(n+Ulog n)，空间复杂度O(n+U)，其中U=max(end)
class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        max_days = max(e[1] for e in events)
        # 按照开始时间分组
        groups = [[] for _ in range(max_days + 1)]
        for start, end in events:
            groups[start].append(end)

        ans = 0
        h = []
        for start, ends in enumerate(groups):
            # 删除过期会议
            while h and h[0] < start:
                heapq.heappop(h)
            # 新增可以参加的会议
            for end in ends:
                heapq.heappush(h, end)
            # 参加一个结束时间最早的会议
            if h:
                ans += 1
                heapq.heappop(h)
        return ans
