from collections import Counter

class Solution:
    def originalDigits(self, s: str) -> str:
        n = Counter(s)
        x0 = n['z']
        x2 = n['w']
        x4 = n['u']
        x6 = n['x']
        x8 = n['g']
        x1 = n['o'] - x0 - x2 - x4
        x3 = n['h'] - x8
        x5 = n['f'] - x4
        x7 = n['s'] - x6
        x9 = n['i'] - x5 - x6 - x8
        x = [x0, x1, x2, x3, x4, x5, x6, x7, x8, x9]
        return ''.join(str(i) * x[i] for i in range(10))
