class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == '0' or num2 == '0':
            return '0'
        a = [int(c) for c in reversed(num1)]
        b = [int(c) for c in reversed(num2)]
        n1 = len(a)
        n2 = len(b)
        res = [0] * (n1 + n2)
        for i in range(n1):
            for j in range(n2):
                tmp = a[i] * b[j] + res[i + j]
                res[i + j] = tmp % 10
                res[i + j + 1] += tmp // 10
        while res[-1] == 0:
            res.pop()
        return ''.join(str(c) for c in reversed(res))
