from collections import defaultdict
from collections import deque

class Solution:
    def __init__(self):
        self.word_id = {}
        self.word_index = 0
        self.graph = defaultdict(list)

    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        self.add_edge(beginWord)
        for word in wordList:
            self.add_edge(word)
        return self.bfs(self.word_id[beginWord], self.word_id[endWord])

    def add_word(self, word):
        if word not in self.word_id:
            self.word_id[word] = self.word_index
            self.word_index += 1

    def add_edge(self, word):
        self.add_word(word)
        id1 = self.word_id[word]
        chars = list(word)
        for k in range(len(chars)):
            tmp, chars[k] = chars[k], '*'
            virtual_word = ''.join(chars)
            self.add_word(virtual_word)
            id2 = self.word_id[virtual_word]
            self.graph[id1].append(id2)
            self.graph[id2].append(id1)
            chars[k] = tmp

    def bfs(self, begin, end):
        visited = [False] * len(self.graph)
        queue = deque([begin])
        length = 0
        while queue:
            length += 1
            for i in range(len(queue)):
                v = queue.popleft()
                if v == end:
                    return length // 2 + 1
                visited[v] = True
                for u in self.graph[v]:
                    if not visited[u]:
                        queue.append(u)
        return 0
