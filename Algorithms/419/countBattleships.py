class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        ans = 0
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == 'X':
                    ans += 1
                    k = j + 1
                    while k < len(board[i]) and board[i][k] == 'X':
                        board[i][k] = '.'
                        k += 1
                    k = i + 1
                    while k < len(board) and board[k][j] == 'X':
                        board[k][j] = '.'
                        k += 1
        return ans
