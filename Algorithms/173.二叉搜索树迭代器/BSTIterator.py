# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: TreeNode):
        self.it = inorder(root)
        self.val = None

    def next(self) -> int:
        if self.val is not None:
            ret, self.val = self.val, None
            return ret
        else:
            return next(self.it)

    def hasNext(self) -> bool:
        try:
            self.val = next(self.it)
            return True
        except StopIteration:
            return False


def inorder(root):
    if not root:
        return
    yield from inorder(root.left)
    yield root.val
    yield from inorder(root.right)


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
