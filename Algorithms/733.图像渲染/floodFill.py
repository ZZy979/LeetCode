from collections import deque

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        if not image:
            return image
        m = len(image)
        n = len(image[0])
        color = image[sr][sc]
        if color == newColor:
            return image
        queue = deque([(sr, sc)])
        while queue:
            x, y = queue.popleft()
            image[x][y] = newColor
            if x >= 1 and image[x - 1][y] == color:
                queue.append((x - 1, y))
            if x < m - 1 and image[x + 1][y] == color:
                queue.append((x + 1, y))
            if y >= 1 and image[x][y - 1] == color:
                queue.append((x, y - 1))
            if y < n - 1 and image[x][y + 1] == color:
                queue.append((x, y + 1))
        return image
