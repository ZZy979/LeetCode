class Solution:
    def longestPalindrome(self, s: str) -> str:
        max_length = 0
        # 奇数长度
        c1 = r1 = 0
        for i in range(len(s)):
            j = 1
            while i - j >= 0 and i + j < len(s) and s[i - j] == s[i + j]:
                j += 1
            j -= 1
            if 2 * j + 1 > max_length:
                max_length = 2 * j + 1
                c1 = i
                r1 = j
        # 偶数长度
        c2 = r2 = 0
        for i in range(len(s) - 1):
            if s[i] == s[i + 1]:
                j = 1
                while i - j >= 0 and i + j + 1 < len(s) and s[i - j] == s[i + j + 1]:
                    j += 1
                j -= 1
                if 2 * j + 2 > max_length:
                    max_length = 2 * j + 2
                    c2 = i
                    r2 = j
        return s[c2 - r2:c2 + r2 + 2] if max_length % 2 == 0 else s[c1 - r1:c1 + r1 + 1]
