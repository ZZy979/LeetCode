from collections import defaultdict

class Solution:
    def __init__(self):
        self.paths = defaultdict(list)
        self.ans = []

    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        for src, dst in tickets:
            self.paths[src].append(dst)
        for start in self.paths:
            self.paths[start].sort(reverse=True)
        self.search('JFK')
        return self.ans[::-1]
    
    def search(self, start):
        while self.paths[start]:
            self.search(self.paths[start].pop())
        self.ans.append(start)
