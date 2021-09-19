# 官方题解：回溯+字典树
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = Trie()
        for word in words:
            trie.insert(word)
        m, n = len(board), len(board[0])
        self.ans = set()
        for r in range(m):
            for c in range(n):
                self.dfs(board, r, c, trie.root, '')
        return list(self.ans)

    def dfs(self, board, r, c, trie, word):
        ch = board[r][c]
        if ch not in trie:
            return
        trie = trie[ch]
        word = word + ch
        if '#' in trie:
            self.ans.add(word)
        
        board[r][c] = '.'
        for nr, nc in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)):
            if 0 <= nr < len(board) and 0 <= nc < len(board[nr]):
                self.dfs(board, nr, nc, trie, word)
        board[r][c] = ch


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
