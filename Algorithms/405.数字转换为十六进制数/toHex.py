class Solution:
    def toHex(self, num: int) -> str:
        if num == 0:
            return '0'
        if num < 0:
            num += 0xffffffff + 1
        chars = []
        hexchars = '0123456789abcdef'
        while num:
            num, r = divmod(num, 16)
            chars.append(hexchars[r])
        return ''.join(reversed(chars))
