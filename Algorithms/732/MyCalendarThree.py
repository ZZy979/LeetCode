from sortedcontainers import SortedDict

# 差分数组
# 时间复杂度O(n²)，空间复杂度O(n)
class MyCalendarThree:

    def __init__(self):
        self.cnt = SortedDict()

    def book(self, startTime: int, endTime: int) -> int:
        self.cnt[startTime] = self.cnt.get(startTime, 0) + 1
        self.cnt[endTime] = self.cnt.get(endTime, 0) - 1
        ans = max_book = 0
        for c in self.cnt.values():
            max_book += c
            ans = max(ans, max_book)
        return ans


# Your MyCalendarThree object will be instantiated and called as such:
# obj = MyCalendarThree()
# param_1 = obj.book(startTime,endTime)
