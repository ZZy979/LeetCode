# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 个人解法：最小绝对差 = min{根节点-左子树最大节点, 右子树最小节点-根节点, 左子树最小绝对差, 右子树最小绝对差}
class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        if not root or not root.left and not root.right:
            return 0x7fffffff
        ans = 0x7fffffff
        if root.left:
            ans = min(ans, root.val - self.find_max(root.left), self.getMinimumDifference(root.left))
        if root.right:
            ans = min(ans, self.find_min(root.right) - root.val, self.getMinimumDifference(root.right))
        return ans
    
    def find_max(self, root):
        while root.right:
            root = root.right
        return root.val
    
    def find_min(self, root):
        while root.left:
            root = root.left
        return root.val
