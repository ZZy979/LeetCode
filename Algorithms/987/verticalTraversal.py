# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict
from itertools import chain

class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        self.nodes = defaultdict(lambda: defaultdict(list))
        self.inorder(root, 0, 0)
        return [
            list(chain.from_iterable(
                sorted(self.nodes[c][r]) for r in sorted(self.nodes[c]))
            ) for c in sorted(self.nodes)
        ]

    def inorder(self, root, row, col):
        if not root:
            return
        self.nodes[col][row].append(root.val)
        self.inorder(root.left, row + 1, col - 1)
        self.inorder(root.right, row + 1, col + 1)
