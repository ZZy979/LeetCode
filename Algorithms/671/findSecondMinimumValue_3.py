# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 评论区解法
class Solution:
    def findSecondMinimumValue(self, root: TreeNode) -> int:
        self.root_val = root.val
        return self.dfs(root)
    
    def dfs(self, root):
        if not root:
            return -1
        if root.val > self.root_val:
            return root.val
        ml, mr = self.dfs(root.left), self.dfs(root.right)
        return min(ml, mr) if ml != -1 and mr != -1 else max(ml, mr)
