class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        ri = rj = 0
        for i in range(8):
            for j in range(8):
                if board[i][j] == 'R':
                    ri, rj = i, j
        ans = 0
        for i in range(ri - 1, -1, -1):
            if (c := board[i][rj]) != '.':
                if c == 'p':
                    ans += 1
                break
        for i in range(ri + 1, 8):
            if (c := board[i][rj]) != '.':
                if c == 'p':
                    ans += 1
                break
        for j in range(rj - 1, -1, -1):
            if (c := board[ri][j]) != '.':
                if c == 'p':
                    ans += 1
                break
        for j in range(rj + 1, 8):
            if (c := board[ri][j]) != '.':
                if c == 'p':
                    ans += 1
                break
        return ans
