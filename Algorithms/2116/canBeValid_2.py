# https://leetcode.cn/problems/check-if-a-parentheses-string-can-be-valid/solutions/1178043/zheng-fan-liang-ci-bian-li-by-endlessche-z8ac/
class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        n = len(s)
        if n % 2 == 1:
            return False
        mn = mx = 0
        for i in range(n):
            if locked[i] == '1':
                d = 1 if s[i] == '(' else -1
                mx += d
                if mx < 0:
                    return False
                mn += d
            else:
                mx += 1
                mn -= 1
            if mn < 0:
                mn = 1
        return mn == 0
