# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# DFS，时间复杂度O(mn)，空间复杂度O(m)，其中m和n分别为A和B的节点数
class Solution:
    def isSubStructure(self, A: TreeNode, B: TreeNode) -> bool:
        if not A or not B:
            return False
        return dfs(A, B) or self.isSubStructure(A.left, B) or self.isSubStructure(A.right, B)


def dfs(a, b):
    if not b:
        return True
    if not a:
        return False
    else:
        return a.val == b.val and dfs(a.left, b.left) and dfs(a.right, b.right)
