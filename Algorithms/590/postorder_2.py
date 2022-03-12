"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

# 方法2：迭代
class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
        ans = []
        stack = [root]
        children_visited = set()
        while stack:
            node = stack[-1]
            if not node.children or node in children_visited:
                ans.append(node.val)
                stack.pop()
            else:
                stack.extend(reversed(node.children))
                children_visited.add(node)
        return ans
