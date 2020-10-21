# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        p_path = []
        self.find_path(root, p, p_path)
        p_path.reverse()
        q_path = []
        self.find_path(root, q, q_path)
        q_path.reverse()
        i = 0
        while i < len(p_path) and i < len(q_path):
            if p_path[i] is not q_path[i]:
                break
            i += 1
        return p_path[i - 1]
    
    def find_path(self, root, node, path):
        if root is None:
            return False
        elif root is node or self.find_path(root.left, node, path) or self.find_path(root.right, node, path):
            path.append(root)
            return True
        else:
            return False
