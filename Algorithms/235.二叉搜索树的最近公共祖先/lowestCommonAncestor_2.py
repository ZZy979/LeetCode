# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.ans = None
    
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.search(root, p, q)
        return self.ans
    
    def search(self, root, p, q):
        if ((root.val - p.val) * (root.val - q.val)) <= 0:
            self.ans = root
        elif root.val < p.val and root.val < q.val:
            self.search(root.right, p, q)
        else:
            self.search(root.left, p, q)
