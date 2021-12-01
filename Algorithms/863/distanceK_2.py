# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 官方题解：DFS+哈希表
class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        self.parent = {}
        self.ans = []
        self.find_parent(root)
        self.dfs(target, None, 0, k)
        return self.ans
    
    def find_parent(self, node):
        if node.left:
            self.parent[node.left.val] = node
            self.find_parent(node.left)
        if node.right:
            self.parent[node.right.val] = node
            self.find_parent(node.right)
    
    def dfs(self, node, prev, depth, k):
        if not node:
            return
        if depth == k:
            self.ans.append(node.val)
            return
        if node.left is not prev:
            self.dfs(node.left, node, depth + 1, k)
        if node.right is not prev:
            self.dfs(node.right, node, depth + 1, k)
        if (p := self.parent.get(node.val)) is not prev:
            self.dfs(p, node, depth + 1, k)
