import re
from collections import deque

# 方法2：BFS，60 ms
class Solution:
    def findMinStep(self, board: str, hand: str) -> int:
        hand = ''.join(sorted(hand))
        queue = deque([(board, hand, 0)])
        visited = {(board, hand)}
        while queue:
            board, hand, step = queue.popleft()
            for i in range(len(board)):
                for j in range(len(hand)):
                    if j > 0 and hand[j] == hand[j - 1]:
                        continue
                    if i > 0 and board[i - 1] == hand[j]:
                        continue
                    if board[i] == hand[j] or i > 0 and board[i] == board[i - 1]:
                        new_board = clear(board[:i] + hand[j] + board[i:])
                        new_hand = hand[:j] + hand[j + 1:]
                        if not new_board:
                            return step + 1
                        if (new_board, new_hand) not in visited:
                            queue.append((new_board, new_hand, step + 1))
                            visited.add((new_board, new_hand))
        return -1


def clear(board):
    n = 1
    while n:
        board, n = re.subn(r'(.)\1{2,}', '', board)
    return board
