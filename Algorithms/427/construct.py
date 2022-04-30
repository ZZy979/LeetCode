"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        return construct_rec(grid, 0, 0, len(grid), len(grid[0]))


def construct_rec(grid, r1, c1, r2, c2):
    if all(grid[r][c] == grid[r1][c1] for r in range(r1, r2) for c in range(c1, c2)):
        return Node(grid[r1][c1], True, None, None, None, None)
    d = (r2 - r1) // 2
    return Node(
        True, False,
        construct_rec(grid, r1, c1, r1 + d, c1 + d),
        construct_rec(grid, r1, c1 + d, r1 + d, c2),
        construct_rec(grid, r1 + d, c1, r2, c1 + d),
        construct_rec(grid, r1 + d, c1 + d, r2, c2)
    )
