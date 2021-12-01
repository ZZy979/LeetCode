import re
from functools import lru_cache

# 方法1：DFS，132 ms
class Solution:
    def findMinStep(self, board: str, hand: str) -> int:
        res = dfs(board, ''.join(sorted(hand)))
        return -1 if res == 0x7fffffff else res


@lru_cache(None)
def dfs(board, hand):
    if not board:
        return 0
    elif not hand:
        return 0x7fffffff
    res = 0x7fffffff
    for i in range(len(board)):
        for j in range(len(hand)):
            if j > 0 and hand[j] == hand[j - 1]:
                continue
            if i > 0 and board[i - 1] == hand[j]:
                continue
            if board[i] == hand[j] or i > 0 and board[i] == board[i - 1]:
                res = min(res, 1 + dfs(clear(board[:i] + hand[j] + board[i:]), hand[:j] + hand[j + 1:]))
    return res


def clear(board):
    n = 1
    while n:
        board, n = re.subn(r'(.)\1{2,}', '', board)
    return board
