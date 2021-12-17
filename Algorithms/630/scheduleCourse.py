import heapq

class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        total, q = 0, []
        for t, d in sorted(courses, key=lambda c: c[1]):
            total += t
            if total > d:
                total += heapq.heappushpop(q, -t)
            else:
                heapq.heappush(q, -t)
        return len(q)
