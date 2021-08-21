class Solution:
    def checkRecord(self, s: str) -> bool:
        a = l = 0
        for c in s:
            if c == 'A':
                a += 1
                if a == 2:
                    return False
            if c == 'L':
                l += 1
                if l == 3:
                    return False
            else:
                l = 0
        return True
