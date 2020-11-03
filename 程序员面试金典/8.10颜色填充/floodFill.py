class Solution:
    def __init__(self):
        self.directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        if image[sr][sc] != newColor:
            self.dfs(image, sr, sc, image[sr][sc], newColor)
        return image

    def dfs(self, image, r, c, old_color, new_color):
        image[r][c] = new_color
        for dr, dc in self.directions:
            new_r, new_c = r + dr, c + dc
            if 0 <= new_r < len(image) and 0 <= new_c < len(image[new_r]) and image[new_r][new_c] == old_color:
                self.dfs(image, new_r, new_c, old_color, new_color)
