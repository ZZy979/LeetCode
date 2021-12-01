# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class CBTInserter:

    def __init__(self, root: TreeNode):
        self.root = root
        self.leaf = deque()
        q = deque([root])
        while q:
            node = q.popleft()
            if not node.left or not node.right:
                self.leaf.append(node)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

    def insert(self, val: int) -> int:
        parent = self.leaf[0]
        node = TreeNode(val)
        self.leaf.append(node)
        if not parent.left:
            parent.left = node
        else:
            parent.right = node
            self.leaf.popleft()
        return parent.val

    def get_root(self) -> TreeNode:
        return self.root


# Your CBTInserter object will be instantiated and called as such:
# obj = CBTInserter(root)
# param_1 = obj.insert(val)
# param_2 = obj.get_root()
