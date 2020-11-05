# 超时，需要优化建图
from collections import deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        wordList.insert(0, beginWord)
        graph = build_graph(wordList)
        return bfs(graph, 0, wordList.index(endWord))


def build_graph(words):
    graph = {i: [] for i in range(len(words))}
    for i in range(len(words)):
        for j in range(i + 1, len(words)):
            if sum(1 for k in range(len(words[i])) if words[i][k] != words[j][k]) == 1:
                graph[i].append(j)
                graph[j].append(i)
    return graph


def bfs(graph, begin, end):
    visited = [False] * len(graph)
    queue = deque([0])
    length = 0
    while queue:
        length += 1
        for i in range(len(queue)):
            v = queue.popleft()
            if v == end:
                return length
            visited[v] = True
            for u in graph[v]:
                if not visited[u]:
                    queue.append(u)
    return 0
