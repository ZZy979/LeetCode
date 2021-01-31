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

    def search_prefix(self, word):
        node = self.root
        prefix = []
        for c in word:
            if c not in node:
                return None
            prefix.append(c)
            node = node[c]
            if '#' in node:
                return ''.join(prefix)


class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        trie = Trie()
        for word in dictionary:
            trie.insert(word)
        return ' '.join(trie.search_prefix(word) or word for word in sentence.split())
