class Node:

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.elem = [Node(None, None) for _ in range(16)]
        self.sz = 0
    
    def _hash(self, key):
        return key % len(self.elem)
    
    def _find(self, key):
        n = self.elem[self._hash(key)]
        while n.next:
            if n.next.key == key:
                break
            n = n.next
        return n
    
    def _resize(self):
        tmp = self.elem
        self.elem = [Node(None, None) for _ in range(2 * len(self.elem))]
        for n in tmp:
            while n.next:
                self.put(n.next.key, n.next.value)
                n = n.next

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        if self.sz >= len(self.elem) * 0.75:
            self._resize()
        n = self._find(key)
        if not n.next:
            n.next = Node(key, value)
            self.sz += 1
        else:
            n.next.value = value

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        n = self._find(key)
        return n.next.value if n.next else -1

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        n = self._find(key)
        if n.next:
            n.next = n.next.next
            self.sz -= 1


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
