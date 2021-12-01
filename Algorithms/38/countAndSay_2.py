class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return '1'
        s = self.countAndSay(n - 1)
        ans = ''
        p = q = 0
        while p < len(s):
            while p < len(s) and s[p] == s[q]:
                p += 1
            ans += str(p - q) + s[q]
            q = p
        return ans
