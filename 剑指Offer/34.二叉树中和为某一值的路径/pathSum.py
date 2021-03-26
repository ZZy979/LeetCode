# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, target: int) -> List[List[int]]:
        if not root:
            return []
        self.ans = []
        self.search(root, target, [])
        return self.ans
    
    def search(self, root, target, path):
        path.append(root.val)
        if not root.left and not root.right and target == root.val:
            self.ans.append(path.copy())
        if root.left:
            self.search(root.left, target - root.val, path)
        if root.right:
            self.search(root.right, target - root.val, path)
        path.pop()
