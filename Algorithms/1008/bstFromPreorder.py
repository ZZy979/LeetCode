# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 递归，时间复杂度O(nlog n)
# 52 ms
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        if not preorder:
            return None
        split = 1
        while split < len(preorder) and preorder[split] < preorder[0]:
            split += 1
        return TreeNode(preorder[0], self.bstFromPreorder(preorder[1:split]), self.bstFromPreorder(preorder[split:]))
