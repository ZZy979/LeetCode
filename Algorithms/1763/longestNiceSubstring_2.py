# 官方题解2：分治
class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        self.max_idx = self.max_len = 0
        self.dfs(s, 0, len(s) - 1)
        return s[self.max_idx:self.max_idx + self.max_len]
    
    def dfs(self, s, start, end):
        if start >= end:
            return
        lower = upper = 0
        for i in range(start, end + 1):
            if s[i].islower():
                lower |= 1 << (ord(s[i]) - ord('a'))
            else:
                upper |= 1 << (ord(s[i]) - ord('A'))
        if lower == upper:
            if end - start + 1 > self.max_len:
                self.max_idx, self.max_len = start, end - start + 1
            return
        
        idx, valid = start, lower & upper
        while idx <= end:
            start = idx
            while idx <= end and valid & (1 << (ord(s[idx].lower()) - ord('a'))):
                idx += 1
            self.dfs(s, start, idx - 1)
            idx += 1
