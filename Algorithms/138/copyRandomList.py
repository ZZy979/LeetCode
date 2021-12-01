"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

# 新旧顶点映射，时间复杂度O(n)，空间复杂度O(n)
# 48 ms
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        vhead = Node(0)
        node_map = {}

        p, q = head, vhead
        while p:
            node_map[p] = q.next = Node(p.val)
            p = p.next
            q = q.next
        
        p, q = head, vhead.next
        while p:
            if p.random:
                q.random = node_map[p.random]
            p, q = p.next, q.next
        return vhead.next
