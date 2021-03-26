class Solution:
    def strToInt(self, str: str) -> int:
        s = str.strip()
        chars = []
        i = 0
        if s and s[0] in '+-':
            chars.append(s[0])
            i += 1
        while i < len(s) and s[i].isdigit():
            chars.append(s[i])
            i += 1
        if not chars or not chars[-1].isdigit():
            return 0
        x = int(''.join(chars))
        return max(-2**31, min(2**31 - 1, x))
