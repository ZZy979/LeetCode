# 官方题解2：计数
class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        slots = 1
        for v in preorder.split(','):
            if slots == 0:
                return False
            elif v == '#':
                slots -= 1
            else:
                slots += 1
        return slots == 0
