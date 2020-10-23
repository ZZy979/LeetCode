# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def BSTSequences(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return [[]]
        left = self.BSTSequences(root.left)
        right = self.BSTSequences(root.right)
        res = []
        for i in left:
            for j in right:
                res.extend([root.val] + z for z in self.mix(i, j))
        return res
    
    def mix(self, l1, l2):
        if not l1 or not l2:
            return [l1 + l2]
        else:
            left = [[l1[0]] + z for z in self.mix(l1[1:], l2)]
            right = [[l2[0]] + z for z in self.mix(l1, l2[1:])]
            return left + right
