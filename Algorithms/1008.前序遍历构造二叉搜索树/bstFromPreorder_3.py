# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 官方题解2：迭代（栈），时间复杂度O(n)
# 36 ms
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        if not preorder:
            return None
        n = len(preorder)
        root = TreeNode(preorder[0])         
        stack = [root]
        for i in range(1, n):
            node, child = stack[-1], TreeNode(preorder[i])
            while stack and stack[-1].val < child.val: 
                node = stack.pop()
            if node.val < child.val:
                node.right = child 
            else:
                node.left = child 
            stack.append(child)
        return root
