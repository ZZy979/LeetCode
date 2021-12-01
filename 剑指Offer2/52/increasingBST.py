# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        vhead = TreeNode(0)
        self.prev = vhead
        self.inorder(root)
        return vhead.right
    
    def inorder(self, root):
        if not root:
            return
        self.inorder(root.left)
        self.prev.right = root
        root.left = None
        self.prev = root
        self.inorder(root.right)
