class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for t in tokens:
            if t == '+':
                stack.append(stack.pop() + stack.pop())
            elif t == '-':
                x = stack.pop()
                stack.append(stack.pop() - x)
            elif t == '*':
                stack.append(stack.pop() * stack.pop())
            elif t == '/':
                x = stack.pop()
                stack.append(int(stack.pop() / x))
            else:
                stack.append(int(t))
        return stack[0]
