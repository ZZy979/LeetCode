# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.cur_mode = []
        self.last = None
        self.count = self.max_count = 0
    
    def findMode(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        self.in_order(root)
        if self.count == self.max_count:
            self.cur_mode.append(self.last)
        elif self.count > self.max_count:
            self.cur_mode = [self.last]
            self.max_count = self.count
        return self.cur_mode
    
    def in_order(self, root):
        if not root:
            return
        self.in_order(root.left)
        if root.val != self.last:
            if self.last is not None:
                if self.count == self.max_count:
                    self.cur_mode.append(self.last)
                elif self.count > self.max_count:
                    self.cur_mode = [self.last]
                    self.max_count = self.count
            self.last = root.val
            self.count = 1
        else:
            self.count += 1
        self.in_order(root.right)
