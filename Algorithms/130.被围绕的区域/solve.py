class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board:
            return
        m = len(board)
        n = len(board[0])
        for y in range(n):
            if board[0][y] == 'O':
                self.dfs(board, 0, y)
            if board[m - 1][y] == 'O':
                self.dfs(board, m - 1, y)
        for x in range(1, m - 1):
            if board[x][0] == 'O':
                self.dfs(board, x, 0)
            if board[x][n - 1] == 'O':
                self.dfs(board, x, n - 1)
        for x in range(m):
            for y in range(n):
                if board[x][y] == 'O':
                    board[x][y] = 'X'
                elif board[x][y] == '.':
                    board[x][y] = 'O'
    
    def dfs(self, board, x, y):
        board[x][y] = '.'
        if x >= 1 and board[x - 1][y] == 'O':
            self.dfs(board, x - 1, y)
        if x < len(board) - 1 and board[x + 1][y] == 'O':
            self.dfs(board, x + 1, y)
        if y >= 1 and board[x][y - 1] == 'O':
            self.dfs(board, x, y - 1)
        if y < len(board[x]) - 1 and board[x][y + 1] == 'O':
            self.dfs(board, x, y + 1)
