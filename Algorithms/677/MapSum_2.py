class MapSum:

    def __init__(self):
        self.root = TrieNode()
        self.data = {}

    def insert(self, key: str, val: int) -> None:
        delta = val - self.data.get(key, 0)
        self.data[key] = val
        node = self.root
        for c in key:
            c = ord(c) - ord('a')
            if not node.child[c]:
                node.child[c] = TrieNode()
            node = node.child[c]
            node.val += delta

    def sum(self, prefix: str) -> int:
        node = self.root
        for c in prefix:
            c = ord(c) - ord('a')
            if not node.child[c]:
                return 0
            node = node.child[c]
        return node.val


class TrieNode:

    def __init__(self):
        self.val = 0
        self.child = [None] * 26


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)
