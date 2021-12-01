from string import ascii_lowercase

class Solution:
    def firstUniqChar(self, s: str) -> int:
        ans = []
        for c in ascii_lowercase:
            i = s.find(c)
            if i != -1 and s.rfind(c) == i:
                ans.append(i)
        return min(ans, default=-1)
