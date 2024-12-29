from sortedcontainers import SortedSet
import heapq

# 官方题解：延迟删除+有序集合+优先队列
class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __lt__(self, other):
        d1 = (self.end - self.start) // 2
        d2 = (other.end - other.start) // 2
        if d1 == d2:
            return self.start < other.start
        return d1 > d2

class ExamRoom:
    def __init__(self, n: int):
        self.n = n
        self.seats = SortedSet()
        self.pq = []

    def seat(self) -> int:
        if not self.seats:
            self.seats.add(0)
            return 0

        left = self.seats[0]
        right = self.n - 1 - self.seats[-1]
        while len(self.seats) >= 2:
            p = self.pq[0]
            start, end = p.start, p.end
            if start in self.seats and end in self.seats and self.seats[self.seats.index(start) + 1] == end: # 不属于延迟删除的区间
                d = end - start
                if d // 2 < right or d // 2 <= left:  # 最左或最右的座位更优
                    break
                heapq.heappop(self.pq)
                mid = start + d // 2
                heapq.heappush(self.pq, Interval(start, mid))
                heapq.heappush(self.pq, Interval(mid, end))
                self.seats.add(mid)
                return mid
            heapq.heappop(self.pq) # leave 函数中延迟删除的区间在此时删除

        if right > left: # 最右的位置更优
            heapq.heappush(self.pq, Interval(self.seats[-1], self.n - 1))
            self.seats.add(self.n - 1)
            return self.n - 1
        else:
            heapq.heappush(self.pq, Interval(0, self.seats[0]))
            self.seats.add(0)
            return 0

    def leave(self, p: int) -> None:
        if p != self.seats[0] and p != self.seats[-1]:
            prev = self.seats[self.seats.index(p) - 1]
            next = self.seats[self.seats.index(p) + 1]
            heapq.heappush(self.pq, Interval(prev, next))
        self.seats.remove(p)
