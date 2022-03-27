class Solution:
    def calPoints(self, ops: List[str]) -> int:
        points = []
        for op in ops:
            if op == '+':
                points.append(points[-1] + points[-2])
            elif op == 'D':
                points.append(2 * points[-1])
            elif op == 'C':
                points.pop()
            else:
                points.append(int(op))
        return sum(points)
