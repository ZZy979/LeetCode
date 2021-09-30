# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 官方题解1：DFS
# 时间复杂度O(n²)，空间复杂度O(n)
# 660 ms
class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> int:
        if not root:
            return 0
        return dfs(root, targetSum) + self.pathSum(root.left, targetSum) + self.pathSum(root.right, targetSum)

def dfs(root, target):
    if not root:
        return 0
    return int(root.val == target) + dfs(root.left, target - root.val) + dfs(root.right, target - root.val)
