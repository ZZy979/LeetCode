# 官方题解：线段树
class SegNode:
    def __init__(self) -> None:
        self.v00 = self.v01 = self.v10 = self.v11 = 0
    
    def set_value(self, v: int) -> None:
        self.v00 = self.v01 = self.v10 = 0
        self.v11 = max(v, 0)
    
    def best(self) -> int:
        return self.v11

class SegTree:
    def __init__(self, n: int) -> None:
        self.n = n
        self.tree = [SegNode() for _ in range(n * 4 + 1)]
    
    def init(self, nums: List[int]) -> None:
        def internal_init(x: int, l: int, r: int) -> None:
            if l == r:
                self.tree[x].set_value(nums[l - 1])
                return
            mid = (l + r) // 2
            internal_init(x * 2, l, mid)
            internal_init(x * 2 + 1, mid + 1, r)
            self.pushup(x)
        internal_init(1, 1, self.n)
    
    def update(self, x: int, v: int) -> None:
        def internal_update(x: int, l: int, r: int, pos: int, v: int) -> None:
            if l > pos or r < pos:
                return
            if l == r:
                self.tree[x].set_value(v)
                return
            mid = (l + r) // 2
            internal_update(x * 2, l, mid, pos, v)
            internal_update(x * 2 + 1, mid + 1, r, pos, v)
            self.pushup(x)
        internal_update(1, 1, self.n, x + 1, v)
    
    def query(self) -> int:
        return self.tree[1].best()

    def pushup(self, x: int) -> None:
        tree_ = self.tree

        l, r = x * 2, x * 2 + 1
        tree_[x].v00 = max(tree_[l].v00 + tree_[r].v10, tree_[l].v01 + tree_[r].v00)
        tree_[x].v01 = max(tree_[l].v00 + tree_[r].v11, tree_[l].v01 + tree_[r].v01)
        tree_[x].v10 = max(tree_[l].v10 + tree_[r].v10, tree_[l].v11 + tree_[r].v00)
        tree_[x].v11 = max(tree_[l].v10 + tree_[r].v11, tree_[l].v11 + tree_[r].v01)

class Solution:
    def maximumSumSubsequence(self, nums: List[int], queries: List[List[int]]) -> int:
        tree = SegTree(len(nums))
        tree.init(nums)
        
        ans = 0
        for x, v in queries:
            tree.update(x, v)
            ans += tree.query()
        return ans % (10**9 + 7)
