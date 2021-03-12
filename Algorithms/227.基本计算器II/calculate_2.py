class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        sign, num = '+', 0
        n = len(s)
        for i, c in enumerate(s):
            if c.isdigit():
                num = 10 * num + int(c)
            if not c.isdigit() and c != ' ' or i == n - 1:
                if sign == '+':
                    stack.append(num)
                elif sign == '-':
                    stack.append(-num)
                elif sign == '*':
                    stack.append(stack.pop() * num)
                else:
                    stack.append(int(stack.pop() / num))
                sign = c
                num = 0
        ans = 0
        while stack:
            ans += stack.pop()
        return ans
