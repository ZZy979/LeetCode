# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        return leaf_seq(root1) == leaf_seq(root2)


def leaf_seq(root):
    if not root.left and not root.right:
        return [root.val]
    res = []
    if root.left:
        res.extend(leaf_seq(root.left))
    if root.right:
        res.extend(leaf_seq(root.right))
    return res
