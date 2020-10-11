class Solution:
    def romanToInt(self, s: str) -> int:
        s = s.replace('CM', 'DCCCC').replace('CD', 'CCCC')\
            .replace('XC', 'LXXXX').replace('XL', 'XXXX')\
            .replace('IX', 'VIIII').replace('IV', 'IIII')
        value = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        return sum(value[c] for c in s)
