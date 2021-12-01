from itertools import chain

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        return validate_rows(board) and validate_columns(board) and validate_subgrids(board)


def validate_rows(board):
    return all(validate(row) for row in board)

def validate_columns(board):
    return all(validate(board[r][c] for r in range(9)) for c in range(9))

def validate_subgrids(board):
    return all(
        validate(chain.from_iterable((board[r][c] for c in range(j * 3, (j + 1)* 3)) for r in range(i * 3, (i + 1) * 3)))
        for i in range(3) for j in range(3)
    )

def validate(nums):
    nums = list(x for x in nums if x != '.')
    return len(nums) == len(set(nums))
