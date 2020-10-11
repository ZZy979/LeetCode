class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        self.update_dfs(board, *click)
        return board
    
    def update_dfs(self, board, x, y):
        if x < 0 or x > len(board) or y < 0 or y > len(board[x]) or board[x][y] not in 'EM':
            return
        if board[x][y] == 'M':
            board[x][y] = 'X'
            return
        r1, rn = x >= 1, x < len(board) - 1
        c1, cn = y >= 1, y < len(board[x]) - 1
        mines = (r1 and board[x - 1][y] == 'M') + (rn and board[x + 1][y] == 'M')\
            + (c1 and board[x][y - 1] == 'M') + (cn and board[x][y + 1] == 'M')\
            + (r1 and c1 and board[x - 1][y - 1] == 'M')\
            + (r1 and cn and board[x - 1][y + 1] == 'M')\
            + (rn and c1 and board[x + 1][y - 1] == 'M')\
            + (rn and cn and board[x + 1][y + 1] == 'M')
        if mines == 0:
            board[x][y] = 'B'
            if r1:
                self.update_dfs(board, x - 1, y)
            if rn:
                self.update_dfs(board, x + 1, y)
            if c1:
                self.update_dfs(board, x, y - 1)
            if cn:
                self.update_dfs(board, x, y + 1)
            if r1 and c1:
                self.update_dfs(board, x - 1, y - 1)
            if r1 and cn:
                self.update_dfs(board, x - 1, y + 1)
            if rn and c1:
                self.update_dfs(board, x + 1, y - 1)
            if rn and cn:
                self.update_dfs(board, x + 1, y + 1)
        else:
            board[x][y] = str(mines)
