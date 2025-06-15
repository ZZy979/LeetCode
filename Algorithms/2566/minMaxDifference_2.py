class Solution:
    def minMaxDifference(self, num: int) -> int:
        s = t = str(num)
        i = 0
        while i < len(s) and s[i] == '9':
            i += 1
        if i < len(s):
            s = s.replace(s[i], '9')
        t = t.replace(t[0], '0')
        return int(s) - int(t)
