from collections import defaultdict

class Solution:
    def countGoodNodes(self, edges: List[List[int]]) -> int:
        self.child = defaultdict(list)
        for a, b in edges:
            self.child[a].append(b)
            self.child[b].append(a)
        self.good_node = 0
        self.seen = {0}
        self.dfs(0)
        return self.good_node
    
    def dfs(self, root):
        self.seen.add(root)
        child_nodes = [self.dfs(c) for c in self.child[root] if c not in self.seen]
        if not child_nodes or all(child_nodes[i] == child_nodes[0] for i in range(1, len(child_nodes))):
            self.good_node += 1
        self.seen.remove(root)
        return sum(child_nodes) + 1
