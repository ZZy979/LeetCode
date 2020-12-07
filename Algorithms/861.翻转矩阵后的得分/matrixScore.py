class Solution:
    def matrixScore(self, A: List[List[int]]) -> int:
        # 通过行翻转使得第1列全部是1
        for r in range(len(A)):
            if A[r][0] == 0:
                invert_row(A, r)
        # 通过列翻转使得其他列1比0多
        for c in range(len(A[0])):
            if count_ones_in_column(A, c) <= len(A) // 2:
                invert_column(A, c)
        return sum(row_score(row) for row in A)


def invert_row(a, r):
    for c in range(len(a[r])):
        a[r][c] = 1 - a[r][c]


def invert_column(a, c):
    for r in range(len(a)):
        a[r][c] = 1 - a[r][c]


def count_ones_in_column(a, c):
    return sum(1 for r in range(len(a)) if a[r][c] == 1)


def row_score(row):
    score = 0
    p = 1
    for c in range(len(row) - 1, -1, -1):
        if row[c] == 1:
            score += p
        p <<= 1
    return score
