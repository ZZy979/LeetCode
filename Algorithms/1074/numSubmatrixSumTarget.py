from collections import Counter

class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        m, n = len(matrix), len(matrix[0])
        ans = 0
        for r1 in range(m):
            col_sum = [0] * n
            for r2 in range(r1, m):
                for c in range(n):
                    col_sum[c] += matrix[r2][c]
                ans += subarraySum(col_sum, target)
        return ans


# 第560题
def subarraySum(nums: List[int], k: int) -> int:
    ans = pre = 0
    c = Counter([0])
    for x in nums:
        pre += x
        ans += c[pre - k]
        c[pre] += 1
    return ans
