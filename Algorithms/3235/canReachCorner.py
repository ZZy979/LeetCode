class Solution:
    def canReachCorner(self, xCorner: int, yCorner: int, circles: List[List[int]]) -> bool:

        def pointInCircle(px: int, py: int, x: int, y: int, r: int) -> bool:
            return (x - px) ** 2 + (y - py) ** 2 <= r ** 2

        def circleIntersectsTopLeftOfRectangle(x: int, y: int, r: int, xCorner: int, yCorner: int) -> bool:
            return (abs(x) <= r and 0 <= y <= yCorner) or (0 <= x <= xCorner and abs(y - yCorner) <= r) or pointInCircle(x, y, 0, yCorner, r)
        
        def circleIntersectsBottomRightOfRectangle(x: int, y: int, r: int, xCorner: int, yCorner: int) -> bool:
            return (abs(y) <= r and 0 <= x <= xCorner) or (0 <= y <= yCorner and abs(x - xCorner) <= r) or (pointInCircle(x, y, xCorner, 0, r))

        def circlesIntersectInRectangle(x1: int, y1: int, r1: int, x2: int, y2: int, r2: int, xCorner: int, yCorner: int) -> bool:
            return (x1 - x2) ** 2 + (y1 - y2) ** 2 <= (r1 + r2) ** 2 and x1 * r2 + x2 * r1 < (r1 + r2) * xCorner and y1 * r2 + y2 * r1 < (r1 + r2) * yCorner

        visited = [False] * len(circles)
        def dfs(i: int) -> bool:
            x1, y1, r1 = circles[i]
            if circleIntersectsBottomRightOfRectangle(x1, y1, r1, xCorner, yCorner):
                return True
            visited[i] = True
            for j, (x2, y2, r2) in enumerate(circles):
                if (not visited[j]) and circlesIntersectInRectangle(x1, y1, r1, x2, y2, r2, xCorner, yCorner) and dfs(j):
                    return True
            return False

        for i, (x, y, r) in enumerate(circles):
            if pointInCircle(0, 0, x, y, r) or pointInCircle(xCorner, yCorner, x, y, r):
                return False
            if (not visited[i]) and circleIntersectsTopLeftOfRectangle(x, y, r, xCorner, yCorner) and dfs(i):
                return False
        return True
