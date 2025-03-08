# 官方题解：动态规划+预处理
# 时间复杂度O(n²k)，空间复杂度O(n²+nk)
class Solution:
    def palindromePartition(self, s: str, k: int) -> int:
        n = len(s)
        cost = [[0] * n for _ in range(n)]  # cost[i][j]表示将s[i..j]变成回文串最少需要修改的字符数
        for span in range(2, n + 1):
            for i in range(n - span + 1):
                j = i + span - 1
                cost[i][j] = cost[i + 1][j - 1] + (s[i] != s[j])

        f = [[10**9] * (k + 1) for _ in range(n + 1)]  # f[i][j]表示将s的前i个字符分割成j个回文串最少需要修改的字符数
        f[0][0] = 0
        for i in range(1, n + 1):
            for j in range(1, min(k, i) + 1):
                if j == 1:
                    f[i][j] = cost[0][i - 1]
                else:
                    for i0 in range(j - 1, i):
                        f[i][j] = min(f[i][j], f[i0][j - 1] + cost[i0][i - 1])
        return f[n][k]
