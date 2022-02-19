class Solution:
    def checkWays(self, pairs: List[List[int]]) -> int:
        adj = defaultdict(set)
        for x, y in pairs:
            adj[x].add(y)
            adj[y].add(x)

        # 检测是否存在根节点
        root = next((node for node, neighbours in adj.items() if len(neighbours) == len(adj) - 1), -1)
        if root == -1:
            return 0

        ans = 1
        for node, neighbours in adj.items():
            if node == root:
                continue

            currDegree = len(neighbours)
            parent = -1
            parentDegree = maxsize
            # 根据 degree 的大小找到 node 的父节点 parent
            for neighbour in neighbours:
                if currDegree <= len(adj[neighbour]) < parentDegree:
                    parent = neighbour
                    parentDegree = len(adj[neighbour])
            # 检测 neighbours 是否为 adj[parent] 的子集
            if parent == -1 or any(neighbour != parent and neighbour not in adj[parent] for neighbour in neighbours):
                return 0

            if parentDegree == currDegree:
                ans = 2
        return ans
