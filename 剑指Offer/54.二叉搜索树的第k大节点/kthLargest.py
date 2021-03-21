# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def kthLargest(self, root: TreeNode, k: int) -> int:
        child_num = child_num_tree(root)
        node = root
        while k != child_num.right.val + 1:
            if k <= child_num.right.val:
                node = node.right
                child_num = child_num.right
            else:
                k -= child_num.right.val + 1
                node = node.left
                child_num = child_num.left
        return node.val


def child_num_tree(root):
    if not root:
        return TreeNode(0)
    left = child_num_tree(root.left)
    right = child_num_tree(root.right)
    node = TreeNode(1 + left.val + right.val)
    node.left = left
    node.right = right
    return node
