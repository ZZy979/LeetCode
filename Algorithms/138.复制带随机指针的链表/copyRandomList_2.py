"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

# 官方题解1：DFS，时间复杂度O(n)，空间复杂度O(n)
# 40 ms
class Solution:

    def __init__(self):
        self.visited = {}

    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return None
        if head in self.visited:
            return self.visited[head]
        self.visited[head] = node = Node(head.val)
        node.next = self.copyRandomList(head.next)
        node.random = self.copyRandomList(head.random)
        return node
