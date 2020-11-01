class TrieNode:

    def __init__(self, letter):
        self.letter = letter
        self.children = []


class Solution:
    def __init__(self):
        self.trie = TrieNode('^')
        self.ans = []
        self.sentence = []

    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        if any([c not in set(''.join(wordDict)) for c in s]):
            return []
        for word in wordDict:
            add_word(self.trie, word, 0)
        self.dfs(self.trie, s, 0, 0)
        return self.ans

    def dfs(self, cur_node, s, start, i):
        if i == len(s):
            if any(child.letter == '#' for child in cur_node.children):
                self.sentence.append(s[start:])
                self.ans.append(' '.join(self.sentence))
                self.sentence.pop()
            return
        for child in cur_node.children:
            if child.letter == s[i]:
                self.dfs(child, s, start, i + 1)
            elif child.letter == '#':
                self.sentence.append(s[start:i])
                self.dfs(self.trie, s, i, i)
                self.sentence.pop()


def add_word(trie, word, start):
    if start == len(word):
        trie.children.append(TrieNode('#'))
        return
    for child in trie.children:
        if child.letter == word[start]:
            add_word(child, word, start + 1)
            break
    else:
        p = trie
        for i in range(start, len(word)):
            q = TrieNode(word[i])
            p.children.append(q)
            p = q
        p.children.append(TrieNode('#'))
