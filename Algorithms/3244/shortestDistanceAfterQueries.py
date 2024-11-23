# 链表
class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        node_map = {}
        for i in range(n - 1, -1, -1):
            node_map[i] = ListNode(i, node_map.get(i + 1))
        ans = []
        for u, v in queries:
            if u in node_map and v in node_map:
                p = node_map[u].next
                while p.value != v:
                    del node_map[p.value]
                    p = p.next
                node_map[u].next = node_map[v]
            ans.append(len(node_map) - 1)
        return ans


class ListNode:
    def __init__(self, value, next):
        self.value = value
        self.next = next
