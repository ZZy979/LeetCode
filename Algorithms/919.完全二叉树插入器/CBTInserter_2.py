# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class CBTInserter:

    def __init__(self, root: TreeNode):
        self.root = root
        self.num_nodes = num_nodes(root)

    def insert(self, val: int) -> int:
        self.num_nodes += 1
        p = self.root
        for b in bin(self.num_nodes)[3:-1]:
            if b == '0':
                p = p.left
            else:
                p = p.right
        if self.num_nodes % 2 == 0:
            p.left = TreeNode(val)
        else:
            p.right = TreeNode(val)
        return p.val

    def get_root(self) -> TreeNode:
        return self.root


def num_nodes(root):
    return 0 if not root else 1 + num_nodes(root.left) + num_nodes(root.right)


# Your CBTInserter object will be instantiated and called as such:
# obj = CBTInserter(root)
# param_1 = obj.insert(val)
# param_2 = obj.get_root()
