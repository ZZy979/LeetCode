class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        m, n = len(img), len(img[0])
        return [[sum(img[i + di][j + dj] for di in range(-1, 2) for dj in range(-1, 2) if 0 <= i + di < m and 0 <= j + dj < n) // sum(0 <= i + di < m and 0 <= j + dj < n for di in range(-1, 2) for dj in range(-1, 2)) for j in range(n)] for i in range(m)]
