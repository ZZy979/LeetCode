# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 官方题解：二分查找+位运算，时间复杂度O(log²n)，空间复杂度O(1)
# 80 ms
class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        level = max_level(root)
        low, high = 1 << level, (1 << (level + 1)) - 1
        while low < high:
            mid = (low + high + 1) // 2
            if exists(root, level, mid):
                low = mid
            else:
                high = mid - 1
        return low


def max_level(root):
    level = 0
    while root.left:
        level += 1
        root = root.left
    return level


def exists(root, level, k):
    bits = 1 << (level - 1)
    while root and bits:
        if bits & k == 0:
            root = root.left
        else:
            root = root.right
        bits >>= 1
    return root is not None
