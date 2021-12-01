# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> int:
        if not root:
            return 0
        return dfs(root, targetSum, False) + dfs(root, targetSum, True)

def dfs(root, target, selected):
    if not root:
        return 0
    if selected:
        return int(root.val == target) + dfs(root.left, target - root.val, True) + dfs(root.right, target - root.val, True)
    else:
        return dfs(root.left, target, True) + dfs(root.right, target, True) + dfs(root.left, target, False) + dfs(root.right, target, False)
