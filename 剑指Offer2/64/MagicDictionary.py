class MagicDictionary:

    def __init__(self):
        self.trie = Trie()

    def buildDict(self, dictionary: List[str]) -> None:
        for word in dictionary:
            self.trie.insert(word)

    def search(self, searchWord: str) -> bool:
        return self.trie.search_replace(searchWord)


class Trie:

    def __init__(self):
        self.root = {}

    def insert(self, word):
        node = self.root
        for c in word:
            if c not in node:
                node[c] = {}
            node = node[c]
        node['#'] = None

    def search_replace(self, word):
        node = self.root
        for i, c in enumerate(word):
            if any(self.search(node[k], word[i + 1:]) for k in node if k != c and k != '#'):
                return True
            elif c in node:
                node = node[c]
            else:
                return False
        return False

    def search(self, root, word):
        node = root
        for c in word:
            if c not in node:
                return False
            node = node[c]
        return node is not None and '#' in node


# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dictionary)
# param_2 = obj.search(searchWord)
