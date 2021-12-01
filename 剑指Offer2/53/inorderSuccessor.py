# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
        self.prev, self.p = None, p
        return self.inorder(root)
    
    def inorder(self, root):
        if not root:
            return None
        if (ans := self.inorder(root.left)) is not None:
            return ans
        elif self.prev is self.p:
            return root
        self.prev = root
        return self.inorder(root.right)
