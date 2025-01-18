from itertools import groupby

class Solution:
    def countTexts(self, pressedKeys: str) -> int:
        q = 10**9 + 7
        f = [1, 1, 2, 4]  # 连续按多次3个字母按键对应的方案数
        g = [1, 1, 2, 4]  # 连续按多次4个字母按键对应的方案数
        n = len(pressedKeys)
        for i in range(n - 3):
            f.append((f[-1] + f[-2] + f[-3]) % q)
            g.append((g[-1] + g[-2] + g[-3] + g[-4]) % q)
        ans = 1
        for c, s in groupby(pressedKeys):
            m = len(list(s))
            ans = ans * (g[m] if c in '79' else f[m]) % q
        return ans
