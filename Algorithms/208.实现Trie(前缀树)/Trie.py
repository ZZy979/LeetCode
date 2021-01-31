class TrieNode:

    def __init__(self, c):
        self.c = c
        self.is_word = False
        self.children = {}

class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode('')

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        node = self.root
        for i, c in enumerate(word):
            if c not in node.children:
                node.children[c] = TrieNode(c)
            node = node.children[c]
            if i == len(word) - 1:
                node.is_word = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        node = self.search_node(word)
        return node is not None and node.is_word
    
    def search_node(self, word: str) -> TrieNode:
        node = self.root
        for c in word:
            if c in node.children:
                node = node.children[c]
            else:
                return None
        return node

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        return self.search_node(prefix) is not None


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
