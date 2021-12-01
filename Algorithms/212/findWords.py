from collections import defaultdict

# DFS（超时）
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        m, n = len(board), len(board[0])
        pos = defaultdict(list)
        for r in range(m):
            for c in range(n):
                pos[board[r][c]].append((r, c))
        return [word for word in words if found(board, pos, word)]


def found(board, pos, word):
    for r, c in pos[word[0]]:
        visited = [[False] * len(board[0]) for _ in range(len(board))]
        if backtrack(board, visited, word, 0, r, c):
            return True
    return False


def backtrack(board, visited, word, i, r, c):
    if i == len(word) - 1:
        return True
    visited[r][c] = True
    for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
        nr, nc = r + dr, c + dc
        if 0 <= nr < len(board) and 0 <= nc < len(board[nr]) and not visited[nr][nc] and board[nr][nc] == word[i + 1]:
            if backtrack(board, visited, word, i + 1, nr, nc):
                return True
    visited[r][c] = False
    return False
