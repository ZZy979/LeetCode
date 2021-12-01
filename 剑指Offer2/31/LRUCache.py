class ListNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.map = {}
        self.head = self.tail = ListNode(None, None)

    def get(self, key: int) -> int:
        if key not in self.map:
            return -1
        node = self.map[key]
        self._remove(node)
        self._set_head(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.map:
            node = self.map[key]
            node.value = value
            self._remove(node)
            self._set_head(node)
        else:
            node = self.map[key] = ListNode(key, value)
            self._set_head(node)
            if len(self.map) > self.capacity:
                del self.map[self.tail.key]
                self._remove(self.tail)

    def _remove(self, node):
        node.prev.next = node.next
        if node is self.tail:
            self.tail = node.prev
        else:
            node.next.prev = node.prev

    def _set_head(self, node):
        node.next = self.head.next
        node.prev = self.head
        self.head.next = node
        if self.tail is self.head:
            self.tail = node
        else:
            node.next.prev = node


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
