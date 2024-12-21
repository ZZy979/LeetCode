import sortedcontainers

# 官方题解：离线算法+有序集合
# 时间复杂度O((n+q)log(n+q))，空间复杂度O(n+q)
class Event:
    def __init__(self, op, size, idx, origin):
        """
        op：事件的类型，0表示房间，1表示查询
        size：房间的size或者查询的minSize
        idx：房间的roomId或者查询的preferred
        origin：房间在数组room中的原始编号或者查询在数组queries中的原始编号
        """
        self.op = op
        self.size = size
        self.idx = idx
        self.origin = origin
    
    def __lt__(self, other):
        return self.size > other.size or (self.size == other.size and self.op < other.op)

class Solution:
    def closestRoom(self, rooms: List[List[int]], queries: List[List[int]]) -> List[int]:
        events = []
        for i, (room_id, size) in enumerate(rooms):
            events.append(Event(0, size, room_id, i))  # 房间事件
        for i, (preferred, min_size) in enumerate(queries):
            events.append(Event(1, min_size, preferred, i))
        events.sort()

        ans = [-1] * len(queries)
        valid = sortedcontainers.SortedList()
        for event in events:
            if event.op == 0:
                valid.add(event.idx)
            else:
                dist = float('inf')
                # 查找最小的大于等于preferred的元素
                x = valid.bisect_left(event.idx)
                if x != len(valid):
                    dist = valid[x] - event.idx
                    ans[event.origin] = valid[x]
                if x != 0:
                    # 查找最大的严格小于preferred的元素
                    x -= 1
                    if event.idx - valid[x] <= dist:
                        ans[event.origin] = valid[x]
        return ans
