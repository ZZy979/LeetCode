class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        words.sort(key=len)
        ans = []
        trie = Trie()
        for word in words:
            if not word:
                continue
            if trie.dfs(word, 0):
                ans.append(word)
            else:
                trie.insert(word)
        return ans


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

    def dfs(self, word, start):
        if start == len(word):
            return True
        node = self.root
        for i in range(start, len(word)):
            if word[i] not in node:
                return False
            node = node[word[i]]
            if '#' in node and self.dfs(word, i + 1):
                return True
        return False
