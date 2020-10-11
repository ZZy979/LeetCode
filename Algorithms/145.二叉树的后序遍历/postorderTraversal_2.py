# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 迭代版本
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        stack = []
        ans = []
        cur = root
        prev = None
        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack[-1]
            if not cur.right or cur.right is prev:
                ans.append(cur.val)
                stack.pop()
                prev, cur = cur, None
            else:
                cur = cur.right
        return ans
