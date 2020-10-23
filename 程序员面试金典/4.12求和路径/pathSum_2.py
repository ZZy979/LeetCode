# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 评论区解法，速度快4倍
class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        self.ans = 0
        prefix_sum = defaultdict(int)
        prefix_sum[0] = 1

        def dfs(node: TreeNode, total: int):
            if node is None:
                return
            total += node.val
            self.ans += prefix_sum[total-sum]
            prefix_sum[total] += 1
            dfs(node.left, total)
            dfs(node.right, total)
            prefix_sum[total] -= 1

        dfs(root, 0)
        return self.ans
