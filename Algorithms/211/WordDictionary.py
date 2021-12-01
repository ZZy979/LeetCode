class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = {}

    def addWord(self, word: str) -> None:
        node = self.root
        for c in word:
            if c not in node:
                node[c] = {}
            node = node[c]
        node['#'] = None

    def search(self, word: str) -> bool:
        return self.search_rec(list(word), 0, self.root)
    
    def search_rec(self, word, i, node):
        if i == len(word):
            return '#' in node
        if word[i] == '.':
            return any(self.search_rec(word, i + 1, node[c]) for c in node if c != '#')
        else:
            return False if word[i] not in node else self.search_rec(word, i + 1, node[word[i]])


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
