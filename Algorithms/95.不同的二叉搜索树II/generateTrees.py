# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        if n == 0:
            return []
        else:
            return self.generate(1, n)
    
    def generate(self, left, right):
        ans = []
        if left > right:
            return [None]
        for i in range(left, right + 1):
            left_nodes = self.generate(left, i - 1)
            right_nodes = self.generate(i + 1, right)
            for left_node in left_nodes:
                for right_node in right_nodes:
                    ans.append(TreeNode(i, left_node, right_node))
        return ans
