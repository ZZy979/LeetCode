class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        self.ans = []
        self.backtrack(s, [])
        return self.ans
    
    def backtrack(self, s, tmp):
        if len(s) == 0 and len(tmp) == 4:
            self.ans.append('.'.join(tmp))
            return
        if len(tmp) < 4:
            for i in range(min(3, len(s))):
                p = s[:i + 1]
                if p and 0 <= int(p) <= 255 and str(int(p)) == p:
                    self.backtrack(s[i + 1:], tmp + [p])
