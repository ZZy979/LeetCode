class ListNode:

    def __init__(self, key='', count=0):
        self.keys = {key}
        self.count = count
        self.prev = self.next = None
    
    def insert(self, node):
        node.prev, node.next = self, self.next
        node.prev.next = node.next.prev = node
        return node
    
    def remove(self):
        self.prev.next = self.next
        self.next.prev = self.prev


class AllOne:

    def __init__(self):
        self.head = ListNode()
        self.head.prev = self.head.next = self.head
        self.nodes = {}

    def inc(self, key: str) -> None:
        if key not in self.nodes:
            if self.head.next is self.head or self.head.next.count > 1:
                self.nodes[key] = self.head.insert(ListNode(key, 1))
            else:
                self.head.next.keys.add(key)
                self.nodes[key] = self.head.next
        else:
            cur = self.nodes[key]
            nxt = cur.next
            if nxt is self.head or nxt.count > cur.count + 1:
                self.nodes[key] = cur.insert(ListNode(key, cur.count + 1))
            else:
                nxt.keys.add(key)
                self.nodes[key] = nxt
            cur.keys.remove(key)
            if not cur.keys:
                cur.remove()

    def dec(self, key: str) -> None:
        cur = self.nodes[key]
        if cur.count == 1:
            del self.nodes[key]
        else:
            pre = cur.prev
            if pre is self.head or pre.count < cur.count - 1:
                self.nodes[key] = cur.prev.insert(ListNode(key, cur.count - 1))
            else:
                pre.keys.add(key)
                self.nodes[key] = pre
        cur.keys.remove(key)
        if not cur.keys:
            cur.remove()

    def getMaxKey(self) -> str:
        return next(iter(self.head.prev.keys)) if self.head.prev is not self.head else ''

    def getMinKey(self) -> str:
        return next(iter(self.head.next.keys)) if self.head.next is not self.head else ''


# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()
