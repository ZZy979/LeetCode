# 官方题解1：栈
class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        stack = [1]
        for v in preorder.split(','):
            if not stack:
                return False
            elif v == '#':
                top = stack.pop() - 1
                if top > 0:
                    stack.append(top)
            else:
                top = stack.pop() - 1
                if top > 0:
                    stack.append(top)
                stack.append(2)
        return len(stack) == 0
