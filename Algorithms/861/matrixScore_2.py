# 官方题解：不修改原矩阵，直接计算每一列对总分数的贡献
class Solution:
    def matrixScore(self, A: List[List[int]]) -> int:
        m, n = len(A), len(A[0])
        score = m * (1 << (n - 1))
        for c in range(1, n):
            n_ones = count_ones_in_column(A, c)
            k = max(n_ones, m - n_ones)
            score += k * (1 << (n - c - 1))
        return score


def count_ones_in_column(a, c):
    # 如果这一行进行了行反转，则该元素的实际取值为1 - A[i][j]
    return sum(a[r][c] if a[r][0] == 1 else 1 - a[r][c] for r in range(len(a)))
