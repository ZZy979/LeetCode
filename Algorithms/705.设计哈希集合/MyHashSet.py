class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.elem = [None] * 16
        self.sz = 0
    
    def _hash(self, key):
        return key % len(self.elem)
    
    def _find(self, key):
        h = self._hash(key)
        while self.elem[h] is not None and self.elem[h] != key:
            h = (h + 1) % len(self.elem)
        return h
    
    def _resize(self):
        tmp = self.elem
        self.elem = [None] * (2 * len(self.elem))
        for v in tmp:
            if v is not None:
                self.add(v)

    def add(self, key: int) -> None:
        if self.sz >= len(self.elem) * 0.75:
            self._resize()
        self.elem[self._find(key)] = key
        self.sz += 1

    def remove(self, key: int) -> None:
        h = self._find(key)
        if self.elem[h] is None:
            return
        self.elem[h] = None
        self.sz -= 1
        nex = (h + 1) % len(self.elem)
        while self.elem[nex] is not None and self._hash(self.elem[nex]) != nex:
            self.elem[h], self.elem[nex] = self.elem[nex], None
            h, nex = nex, (nex + 1) % len(self.elem)

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        return self.elem[self._find(key)] == key


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
