# 位运算
class Solution:
    def validStrings(self, n: int) -> List[str]:
        res = []
        mask = (1 << n) - 1
        for i in range(1 << n):
            t = mask ^ i
            if not (t >> 1 & t):
                res.append(f'{i:0{n}b}')
        return res
