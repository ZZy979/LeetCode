# 官方题解2：栈
class Solution:
    def checkValidString(self, s: str) -> bool:
        left_stack = []
        star_stack = []
        for i, c in enumerate(s):
            if c == '(':
                left_stack.append(i)
            elif c == '*':
                star_stack.append(i)
            else:
                if not left_stack and not star_stack:
                    return False
                elif left_stack:
                    left_stack.pop()
                else:
                    star_stack.pop()
        while left_stack and star_stack:
            if left_stack[-1] > star_stack[-1]:
                return False
            left_stack.pop()
            star_stack.pop()
        return not left_stack
