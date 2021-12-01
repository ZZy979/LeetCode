class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if (len(a) < len(b)):
            a, b = b, a
        x = list(map(int, reversed(a)))
        y = list(map(int, reversed(b)))
        s = [0] * len(x)
        c = 0
        for i in range(len(y)):
            s[i] = x[i] ^ y[i] ^ c
            c = x[i] & c | y[i] & c | x[i] & y[i]
        for i in range(len(y), len(x)):
            s[i] = x[i] ^ c
            c = x[i] & c
        if c:
            s.append(c)
        return ''.join(map(str, reversed(s)))
