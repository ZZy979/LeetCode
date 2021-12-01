# 官方题解：动态规划，36 ms
class Solution:
    def translateNum(self, num: int) -> int:
        num = str(num)
        # f[i]表示num[:i]的翻译方法数
        p, q, r = 0, 0, 1  # f[n - 2], f[n - 1], f[n]
        for i in range(len(num)):
            p, q = q, r
            r = q + p * int(i > 0 and 10 <= int(num[i - 1:i + 1]) <= 25)
        return r
