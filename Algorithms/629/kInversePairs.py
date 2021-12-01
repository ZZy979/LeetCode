# 递推公式，时间复杂度O(min{n^4,k^2})，超时
class Solution:
    def kInversePairs(self, n: int, k: int) -> int:
        # 设1~n的排列中恰好有k个逆序对的个数为p(n, k), 0 <= k <= (n(n-1))/2
        # 对于1~n-1的排列，将n插入不同位置，逆序对分别增加0, 1, ..., n-1
        # p(n, k) = sum_{i = max{0, k-n+1}}^{min{(n-1)(n-2)/2, k}} p(n-1, i)
        # 例如：p(3) = [1, 2, 2, 1]
        #    k=0  1  2  3  4  5  6
        #      1  2  2  1
        #         1  2  2  1
        #            1  2  2  1
        #               1  2  2  1
        # p(4)=1  3  5  6  5  3  1
        upper = [k]
        for m in range(n, 0, -1):
            upper.append(min(((m - 1) * (m - 2)) // 2, k))
        upper.reverse()

        p = [1]
        q = 10**9 + 7
        for m in range(2, n + 1):
            p = [sum(p[i] for i in range(max(0, j - m + 1), min(((m - 1) * (m - 2)) // 2, j, upper[m - 1]) + 1)) % q for j in range(upper[m] + 1)]
        return p[k]
