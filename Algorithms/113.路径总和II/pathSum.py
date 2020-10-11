# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:

    def __init__(self):
        self.ans = []
    
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        if not root:
            return []
        self.dfs(root, sum, [])
        return self.ans
    
    def dfs(self, root, s, path):
        path.append(root.val)
        if root.val == s and not root.left and not root.right:
            self.ans.append(path.copy())
        if root.left:
            self.dfs(root.left, s - root.val, path)
        if root.right:
            self.dfs(root.right, s - root.val, path)
        path.pop()
