# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        return self.create_tree(nums, 0, len(nums))
    
    def create_tree(self, nums, left, right):
        if left >= right:
            return None
        m = (left + right) // 2
        root = TreeNode(nums[m])
        root.left = self.create_tree(nums, left, m)
        root.right = self.create_tree(nums, m + 1, right)
        return root
