class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        i = 0
        for x in popped:
            if stack and stack[-1] == x:
                stack.pop()
            else:
                while i < len(pushed) and pushed[i] != x:
                    stack.append(pushed[i])
                    i += 1
                if i == len(pushed):
                    return False
                else:
                    i += 1
        return True
