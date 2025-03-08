# 官方题解：动态规划
# 时间复杂度O(n²)，空间复杂度O(n²)
class Solution:
    def checkPartitioning(self, s: str) -> bool:
        n = len(s)
        g = [[True] * n for _ in range(n)]  # g[i][j]表示s[i..j]是否为回文串
        for span in range(2, n + 1):
            for i in range(n - span + 1):
                j = i + span - 1
                g[i][j] = s[i] == s[j] and g[i + 1][j - 1]

        # 遍历中间子串的起止位置
        for start in range(1, n - 1):
            if not g[0][start - 1]:
                continue
            for end in range(start, n - 1):
                if g[start][end] and g[end + 1][n - 1]:
                    return True
        return False
