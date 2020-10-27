# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 迭代版本
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        ans = []
        stack = []
        cur = root
        while cur or stack:
            while cur:
                ans.append(cur.val)
                if cur.right:
                    stack.append(cur.right)
                cur = cur.left
            if stack:
                cur = stack.pop()
        return ans
