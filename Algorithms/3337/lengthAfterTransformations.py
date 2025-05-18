C = 26
Q = 10**9 + 7

# 矩阵快速幂，时间复杂度O(n+C³log t)，空间复杂度O(C²)，其中C=26
class Solution:
    def lengthAfterTransformations(self, s: str, t: int, nums: List[int]) -> int:
        a = create_matrix(nums)
        v = create_vector(s)
        res = mat_mul(v, mat_pow(a, t))
        return sum(res[0][i] for i in range(C)) % Q

def create_matrix(nums):
    a = [[0] * C for _ in range(C)]
    for i in range(C):
        for j in range(nums[i]):
            a[i][(i + j + 1) % C] = 1
    return a

def create_vector(s):
    v = [[0] * C]
    for c in s:
        v[0][ord(c) - ord('a')] += 1
    return v

def mat_mul(a, b):
    m, n, p = len(a), len(a[0]), len(b[0])
    return [[sum(a[i][k] * b[k][j] for k in range(n)) % Q for j in range(p)] for i in range(m)]

def mat_pow(a, p):
    n = len(a)
    res = [[int(j == i) for j in range(n)] for i in range(n)]
    while p > 0:
        if p % 2 == 1:
            res = mat_mul(res, a)
        a = mat_mul(a, a)
        p //= 2
    return res
