class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        visited = [[False] * n for i in range(m)]
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0] and self.dfs(board, m, n, visited, word, i, j, 0):
                    return True
        return False
    
    def dfs(self, board, m, n, visited, word, x, y, w):
        if w == len(word) - 1:
            return True
        visited[x][y] = True
        found = False
        for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            if not found and 0 <= x + dx < m and 0 <= y + dy < n and not visited[x + dx][y + dy] and board[x + dx][y + dy] == word[w + 1]:
                found = self.dfs(board, m, n, visited, word, x + dx, y + dy, w + 1)
                if found:
                    break
        visited[x][y] = False
        return found
