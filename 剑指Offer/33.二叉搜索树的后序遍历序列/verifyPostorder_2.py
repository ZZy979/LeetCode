# 单调栈
class Solution:
    def verifyPostorder(self, postorder: List[int]) -> bool:
        stack, root = [], 0x7fffffff
        for i in range(len(postorder) - 1, -1, -1):
            if postorder[i] > root:
                return False
            while stack and postorder[i] < stack[-1]:
                root = stack.pop()
            stack.append(postorder[i])
        return True
