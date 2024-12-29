from itertools import pairwise
from sortedcontainers import SortedList

# 有序集合+暴力法
class ExamRoom:

    def __init__(self, n: int):
        self.students = SortedList()
        self.n = n

    def seat(self) -> int:
        if not self.students:
            s = 0
        elif len(self.students) == 1:
            s = 0 if self.students[0] >= (self.n - 1) / 2 else self.n - 1
        else:
            s1, s2 = max(itertools.pairwise(self.students), key=lambda p: (p[1] - p[0]) // 2)
            dist = (s2 - s1) // 2
            s = s1 + dist
            if self.n - 1 - self.students[-1] > dist:
                dist, s = self.n - 1 - self.students[-1], self.n - 1
            if self.students[0] >= dist:
                dist, s = self.students[0], 0
        self.students.add(s)
        return s

    def leave(self, p: int) -> None:
        self.students.remove(p)


# Your ExamRoom object will be instantiated and called as such:
# obj = ExamRoom(n)
# param_1 = obj.seat()
# obj.leave(p)