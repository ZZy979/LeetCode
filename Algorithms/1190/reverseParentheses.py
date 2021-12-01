class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        for c in s:
            if c == ')':
                tmp_stack = []
                while (x := stack.pop()) != '(':
                    tmp_stack.append(x)
                stack.extend(tmp_stack)
            else:
                stack.append(c)
        return ''.join(stack)
