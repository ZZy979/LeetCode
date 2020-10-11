# 官方题解
class UnionFind:
    def __init__(self, n):
        self.ancestor = list(range(n))
    
    def union(self, index1: int, index2: int):
        self.ancestor[self.find(index1)] = self.find(index2)
    
    def find(self, index: int) -> int:
        if self.ancestor[index] != index:
            self.ancestor[index] = self.find(self.ancestor[index])
        return self.ancestor[index]

class Solution:
    def findRedundantDirectedConnection(self, edges: List[List[int]]) -> List[int]:
        nodesCount = len(edges)
        uf = UnionFind(nodesCount + 1)
        parent = list(range(nodesCount + 1))
        conflict = -1
        cycle = -1
        for i, (node1, node2) in enumerate(edges):
            if parent[node2] != node2:
                conflict = i
            else:
                parent[node2] = node1
                if uf.find(node1) == uf.find(node2):
                    cycle = i
                else:
                    uf.union(node1, node2)

        if conflict < 0:
            return [edges[cycle][0], edges[cycle][1]]
        else:
            conflictEdge = edges[conflict]
            if cycle >= 0:
                return [parent[conflictEdge[1]], conflictEdge[1]]
            else:
                return [conflictEdge[0], conflictEdge[1]]
