# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        return not root or is_mirror(root.left, root.right)


def is_mirror(root1, root2):
    if not root1 and not root2:
        return True
    elif not root1 or not root2:
        return False
    else:
        return root1.val == root2.val and is_mirror(root1.left, root2.right) and is_mirror(root1.right, root2.left)
