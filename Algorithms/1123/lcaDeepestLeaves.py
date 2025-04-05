# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        return dfs(root)[1]

def dfs(root):
    if not root:
        return 0, None
    left_depth, left_lca = dfs(root.left)
    right_depth, right_lca = dfs(root.right)
    if left_depth == right_depth:
        return left_depth + 1, root
    elif left_depth > right_depth:
        return left_depth + 1, left_lca
    else:
        return right_depth + 1, right_lca
