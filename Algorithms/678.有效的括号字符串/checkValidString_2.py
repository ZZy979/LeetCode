# 官方题解3：记录未匹配左括号数量
class Solution:
    def checkValidString(self, s: str) -> bool:
        lo = hi = 0
        for c in s:
            if c == '(':
                lo += 1
                hi += 1
            elif c == ')':
                lo = max(0, lo - 1)
                hi -= 1
                if hi < 0:
                    return False
            else:
                lo = max(0, lo - 1)
                hi += 1
        return lo <= 0
