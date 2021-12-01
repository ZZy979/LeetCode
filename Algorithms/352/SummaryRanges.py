import bisect

# 二分查找
class SummaryRanges:

    def __init__(self):
        self.nums = []

    def addNum(self, val: int) -> None:
        i = bisect.bisect_left(self.nums, val)
        if not (i < len(self.nums) and self.nums[i] == val):
            self.nums.insert(i, val)

    def getIntervals(self) -> List[List[int]]:
        if not self.nums:
            return []
        intervals = []
        begin = self.nums[0]
        for i in range(1, len(self.nums)):
            if self.nums[i] != self.nums[i - 1] + 1:
                intervals.append([begin, self.nums[i - 1]])
                begin = self.nums[i]
        intervals.append([begin, self.nums[-1]])
        return intervals


# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(val)
# param_2 = obj.getIntervals()
