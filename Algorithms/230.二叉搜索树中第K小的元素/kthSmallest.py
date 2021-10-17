# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.cur = 1

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if not root:
            return None
        if (x := self.kthSmallest(root.left, k)) is not None:
            return x
        if self.cur == k:
            return root.val
        self.cur += 1
        if (x := self.kthSmallest(root.right, k)) is not None:
            return x
        return None
