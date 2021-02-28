class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        visited = [[False] * n for _ in range(m)]
        for r in range(m):
            for c in range(n):
                if board[r][c] == word[0] and dfs(board, visited, word, r, c, 0):
                    return True
        return False


def dfs(board, visited, word, r, c, i):
    if i == len(word) - 1:
        return True
    visited[r][c] = True
    found = False
    for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
        nr, nc = r + dr, c + dc
        if 0 <= nr < len(board) and 0 <= nc < len(board[nr]) and not visited[nr][nc] and board[nr][nc] == word[i + 1]:
            if dfs(board, visited, word, nr, nc, i + 1):
                found = True
                break
    visited[r][c] = False
    return found
