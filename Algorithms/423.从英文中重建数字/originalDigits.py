from collections import Counter

class Solution:
    def originalDigits(self, s: str) -> str:
        n = Counter(s)
        x = [n['z'], n['o'] - n['z'] - n['w'] - n['u'], n['w'], n['h'] - n['g'], n['u'], n['f'] - n['u'], n['x'], n['s'] - n['x'], n['g'], n['i'] - n['f'] + n['u'] - n['x'] - n['g']]
        return ''.join(str(i) * x[i] for i in range(10))
