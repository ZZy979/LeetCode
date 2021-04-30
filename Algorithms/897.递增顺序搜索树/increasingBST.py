# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        vhead = self.p = TreeNode(0)
        self.inorder(root)
        return vhead.right
    
    def inorder(self, root):
        if not root:
            return
        self.inorder(root.left)
        self.p.right = TreeNode(root.val)
        self.p = self.p.right
        self.inorder(root.right)
