# 官方题解：动态规划+前缀和优化，时间复杂度O(n+k²)，空间复杂度O(k)
class Solution:
    def possibleStringCount(self, word: str, k: int) -> int:
        mod = 10**9 + 7
        n, cnt = len(word), 1
        freq = []
        for i in range(1, n):
            if word[i] == word[i - 1]:
                cnt += 1
            else:
                freq.append(cnt)
                cnt = 1
        freq.append(cnt)

        ans = 1
        for o in freq:
            ans = ans * o % mod

        if len(freq) >= k:
            return ans

        # f(i, j)表示用freq中下标<=i的部分构造字符串，并且构造的字符串长度=j的方案数
        # g(i, :)是f(i, :)的前缀和
        f, g = [1] + [0] * (k + 1), [1] * k
        for i in range(len(freq)):
            f_new = [0] * k
            for j in range(1, k):
                f_new[j] = g[j - 1]
                if j - freq[i] - 1 >= 0:
                    f_new[j] = (f_new[j] - g[j - freq[i] - 1]) % mod
            g_new = [f_new[0]] + [0] * (k - 1)
            for j in range(1, k):
                g_new[j] = (g_new[j - 1] + f_new[j]) % mod
            f, g = f_new, g_new
        return (ans - g[k - 1]) % mod
