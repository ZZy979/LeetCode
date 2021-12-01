# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 官方题解1：递归，时间复杂度O(n)
# 48 ms
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        self.idx = 0
        return self.build(preorder, 0, 0x7fffffff)
    
    def build(self, preorder, lower, upper):
        if self.idx == len(preorder):
            return None
        val = preorder[self.idx]
        if not lower <= val <= upper:
            return None
        self.idx += 1
        left = self.build(preorder, lower, val)
        right = self.build(preorder, val, upper)
        return TreeNode(val, left, right)
