class Solution:
    def nearestPalindromic(self, n: str) -> str:
        if int(n) < 10 or int(n[::-1]) == 1:
            return str(int(n) - 1)
        if n == '11':
            return '9'
        if set(n) == {'9'}:
            return str(int(n) + 2)
        a, b = n[:(len(n) + 1) // 2], n[(len(n) + 1) // 2:]
        candidates = [x + x[len(b) - 1::-1] for x in (str(int(a) - 1), a, str(int(a) + 1))]
        return min(candidates, key=lambda x: abs(int(x) - int(n)) or float('inf'))
