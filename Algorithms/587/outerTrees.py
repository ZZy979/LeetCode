class Solution:
    def outerTrees(self, trees: List[List[int]]) -> List[List[int]]:
        def cross(p: List[int], q: List[int], r: List[int]) -> int:
            return (q[0] - p[0]) * (r[1] - q[1]) - (q[1] - p[1]) * (r[0] - q[0])

        n = len(trees)
        if n < 4:
            return trees

        leftMost = 0
        for i, tree in enumerate(trees):
            if tree[0] < trees[leftMost][0]:
                leftMost = i

        ans = []
        vis = [False] * n
        p = leftMost
        while True:
            q = (p + 1) % n
            for r, tree in enumerate(trees):
                # // 如果 r 在 pq 的右侧，则 q = r
                if cross(trees[p], trees[q], tree) < 0:
                    q = r
            # 是否存在点 i, 使得 p q i 在同一条直线上
            for i, b in enumerate(vis):
                if not b and i != p and i != q and cross(trees[p], trees[q], trees[i]) == 0:
                    ans.append(trees[i])
                    vis[i] = True
            if not vis[q]:
                ans.append(trees[q])
                vis[q] = True
            p = q
            if p == leftMost:
                break
        return ans
