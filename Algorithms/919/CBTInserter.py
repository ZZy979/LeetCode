# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class CBTInserter:

    def __init__(self, root: TreeNode):
        self.vals = bfs(root)

    def insert(self, val: int) -> int:
        self.vals.append(val)
        return self.vals[(len(self.vals) - 2) // 2]

    def get_root(self) -> TreeNode:
        root = TreeNode(self.vals[0])
        q = deque([root])
        i = 1
        while i < len(self.vals):
            node = q.popleft()
            node.left = TreeNode(self.vals[i])
            q.append(node.left)
            i += 1
            if i < len(self.vals):
                node.right = TreeNode(self.vals[i])
                q.append(node.right)
                i += 1
        return root


def bfs(root):
    res = []
    q = deque([root])
    while q:
        node = q.popleft()
        res.append(node.val)
        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)
    return res


# Your CBTInserter object will be instantiated and called as such:
# obj = CBTInserter(root)
# param_1 = obj.insert(val)
# param_2 = obj.get_root()
