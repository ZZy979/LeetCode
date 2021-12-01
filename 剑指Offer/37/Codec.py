# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import json
from collections import deque

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return '[]'
        q = deque([root])
        level_order = []
        while q:
            node = q.popleft()
            if not node:
                level_order.append(None)
            else:
                level_order.append(node.val)
                q.append(node.left)
                q.append(node.right)
        return json.dumps(level_order)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        level_order = json.loads(data)
        if not level_order:
            return None
        root = TreeNode(level_order[0])
        q = deque([root])
        i = 1
        while i < len(level_order):
            node = q.popleft()
            if level_order[i] is not None:
                node.left = TreeNode(level_order[i])
                q.append(node.left)
            if level_order[i + 1] is not None:
                node.right = TreeNode(level_order[i + 1])
                q.append(node.right)
            i += 2
        return root

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
