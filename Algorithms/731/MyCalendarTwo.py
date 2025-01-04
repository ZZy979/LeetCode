# 方法一：直接遍历
# 时间复杂度O(n²)，空间复杂度O(n)
class MyCalendarTwo:

    def __init__(self):
        self.booked = []
        self.overlaps = []

    def book(self, startTime: int, endTime: int) -> bool:
        if any(s < endTime and startTime < e for s, e in self.overlaps):
            return False
        for s, e in self.booked:
            if s < endTime and startTime < e:
                self.overlaps.append((max(s, startTime), min(e, endTime)))
        self.booked.append((startTime, endTime))
        return True


# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(startTime,endTime)
