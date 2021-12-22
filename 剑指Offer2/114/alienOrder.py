from collections import defaultdict, deque

class Solution:
    def alienOrder(self, words: List[str]) -> str:
        letters = set(''.join(words))
        edges = defaultdict(list)
        indegrees = defaultdict(int)
        for i in range(len(words) - 1):
            a, b = words[i], words[i + 1]
            if a.startswith(b) and len(a) > len(b):
                return ''
            if (d := first_diff(a, b)) < min(len(a), len(b)):
                u, v = a[d], b[d]
                edges[u].append(v)
                indegrees[v] += 1

        q = deque(u for u in letters if indegrees[u] == 0)
        ans = []
        while q:
            u = q.popleft()
            ans.append(u)
            for v in edges[u]:
                indegrees[v] -= 1
                if indegrees[v] == 0:
                    q.append(v)
        return ''.join(ans) if len(ans) == len(indegrees) else ''


def first_diff(s, t):
    i = 0
    while i < len(s) and i < len(t):
        if s[i] != t[i]:
            break
        i += 1
    return i
