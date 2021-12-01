# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 中序遍历，时间复杂度O(n)
# 264 ms
class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        self.s = 0
        self.inorder(root, low, high)
        return self.s
    
    def inorder(self, root, low, high):
        if not root:
            return
        self.inorder(root.left, low, high)
        if low <= root.val <= high:
            self.s += root.val
        self.inorder(root.right, low, high)
