# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ''
        left_str, right_str = self.tree2str(root.left), self.tree2str(root.right)
        if not left_str and not right_str:
            return str(root.val)
        elif len(left_str) > 0 and not right_str:
            return f'{root.val}({left_str})'
        else:
            return f'{root.val}({left_str})({right_str})'
