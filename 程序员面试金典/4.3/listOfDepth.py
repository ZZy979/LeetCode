# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from collections import deque

class Solution:
    def listOfDepth(self, tree: TreeNode) -> List[ListNode]:
        if tree is None:
            return []
        queue = deque()
        queue.append((tree, 0))
        cur_level = -1
        ans = []
        layer = None
        while queue:
            node, level = queue.popleft()
            if level != cur_level:
                cur_level = level
                if layer is not None:
                    ans.append(layer)
                layer = ListNode(node.val)
                p = layer
            else:
                p.next = ListNode(node.val)
                p = p.next
            if node.left is not None:
                queue.append((node.left, level + 1))
            if node.right is not None:
                queue.append((node.right, level + 1))
        ans.append(layer)
        return ans
