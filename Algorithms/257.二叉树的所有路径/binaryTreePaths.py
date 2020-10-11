# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.ans = []
    
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if root:
            self.dfs(root, [])
        return self.ans
    
    def dfs(self, root, path):
        path.append(root.val)
        if not root.left and not root.right:
            self.ans.append('->'.join(map(str, path)))
        if root.left:
            self.dfs(root.left, path)
        if root.right:
            self.dfs(root.right, path)
        path.pop()
