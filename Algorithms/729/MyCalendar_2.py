from sortedcontainers import SortedDict

# 方法二：有序集合+二分查找
# 时间复杂度：O(nlog n)，空间复杂度：O(n)
class MyCalendar:

    def __init__(self):
        self.booked = SortedDict()

    def book(self, startTime: int, endTime: int) -> bool:
        i = self.booked.bisect_left(endTime)
        if i == 0 or self.booked.items()[i - 1][1] <= startTime:
            self.booked[startTime] = endTime
            return True
        return False


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(startTime,endTime)
