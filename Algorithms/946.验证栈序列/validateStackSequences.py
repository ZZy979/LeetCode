class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        j = 0
        for x in pushed:
            stack.append(x)
            while j < len(popped) and stack and stack[-1] == popped[j]:
                stack.pop()
                j += 1
        return j == len(popped)
