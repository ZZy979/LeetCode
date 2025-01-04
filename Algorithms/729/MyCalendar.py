# 方法一：直接遍历
# 时间复杂度O(n²)，空间复杂度O(n)
class MyCalendar:

    def __init__(self):
        self.booked = []

    def book(self, startTime: int, endTime: int) -> bool:
        if any(s < endTime and startTime < e for s, e in self.booked):
            return False
        self.booked.append((startTime, endTime))
        return True


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(startTime,endTime)
