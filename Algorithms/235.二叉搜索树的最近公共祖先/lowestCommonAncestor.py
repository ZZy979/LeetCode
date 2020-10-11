# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        p_path = []
        q_path = []
        self.search(root, p.val, p_path)
        self.search(root, q.val, q_path)
        i = 0
        while i < min(len(p_path), len(q_path)) - 1:
            if p_path[i] != q_path[i]:
                break
            i += 1
        return p_path[i] if p_path[i] is q_path[i] else p_path[i - 1]
    
    def search(self, root, x, path):
        path.append(root)
        if x == root.val:
            return True
        elif x < root.val:
            return root.left and self.search(root.left, x, path)
        else:
            return root.right and self.search(root.right, x, path)
