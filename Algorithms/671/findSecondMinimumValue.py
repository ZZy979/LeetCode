# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: TreeNode) -> int:
        ans = self.dfs(root)
        return -1 if ans == 0xffffffff else ans

    def dfs(self, root):
        if not root or not root.left:
            return 0xffffffff
        ml, mr = self.dfs(root.left), self.dfs(root.right)
        return sorted({root.left.val, root.right.val, ml, mr})[1]
