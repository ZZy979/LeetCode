# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import Counter

# 官方题解2：前缀和
# 时间复杂度O(n)，空间复杂度O(n)
# 44 ms
class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> int:
        presum = Counter({0: 1})
        return dfs(root, presum, targetSum, 0)


def dfs(root, presum, target, cur):
    if not root:
        return 0
    cur += root.val
    ans = presum[cur - target]
    presum[cur] += 1
    ans += dfs(root.left, presum, target, cur) + dfs(root.right, presum, target, cur)
    presum[cur] -= 1
    return ans
