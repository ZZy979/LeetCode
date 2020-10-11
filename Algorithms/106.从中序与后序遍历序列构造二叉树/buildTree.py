# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if not inorder:
            return None
        root = TreeNode(postorder[-1])
        n_left = inorder.index(root.val)
        n_right = len(inorder) - n_left - 1
        root.left = self.buildTree(inorder[:n_left], postorder[:n_left])
        root.right = self.buildTree(inorder[n_left + 1:], postorder[n_left:n_left + n_right])
        return root
