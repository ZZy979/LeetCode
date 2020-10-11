"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = []):
        self.val = val
        self.neighbors = neighbors
"""
from collections import deque

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return node
        nodes = {node.val: Node(node.val, [])}
        queue = deque([node])
        while queue:
            v = queue.popleft()
            for n in v.neighbors:
                if n.val not in nodes:
                    nodes[n.val] = Node(n.val, [])
                    queue.append(n)
                nodes[v.val].neighbors.append(nodes[n.val])
        return nodes[node.val]
