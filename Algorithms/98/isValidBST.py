# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 中序遍历
class Solution:
    def __init__(self):
        self.prev = float('-inf')
        self.ans = True

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.inorder(root)
        return self.ans

    def inorder(self, root):
        if not root:
            return
        self.inorder(root.left)
        if self.prev >= root.val:
            self.ans = False
        self.prev = root.val
        self.inorder(root.right)
