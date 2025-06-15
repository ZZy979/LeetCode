class Solution:
    def maxDiff(self, num: int) -> int:
        return get_max(num) - get_min(num)

def get_max(num):
    s = str(num)
    i = 0
    while i < len(s) and s[i] == '9':
        i += 1
    if i < len(s):
        s = s.replace(s[i], '9')
    return int(s)

def get_min(num):
    s = str(num)
    if s[0] != '1':
        s = s.replace(s[0], '1')
    else:
        i = 1
        while i < len(s) and (s[i] == '0' or s[i] == s[0]):
            i += 1
        if i < len(s):
            s = s.replace(s[i], '0')
    return int(s)
