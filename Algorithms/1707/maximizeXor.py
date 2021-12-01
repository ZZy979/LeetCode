# 官方题解1：离线询问+字典树
# 7308 ms
class Trie:

    def __init__(self):
        self.left = None
        self.right = None

    def insert(self, val: int):
        node = self
        for i in range(30, -1, -1):
            bit = (val >> i) & 1
            if bit == 0:
                if not node.left:
                    node.left = Trie()
                node = node.left
            else:
                if not node.right:
                    node.right = Trie()
                node = node.right
    
    def getMaxXor(self, val: int) -> int:
        ans, node = 0, self
        for i in range(30, -1, -1):
            bit = (val >> i) & 1
            check = False
            if bit == 0:
                if node.right:
                    node = node.right
                    check = True
                else:
                    node = node.left
            else:
                if node.left:
                    node = node.left
                    check = True
                else:
                    node = node.right
            if check:
                ans |= 1 << i
        return ans


class Solution:
    def maximizeXor(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        n, q = len(nums), len(queries)
        nums.sort()
        queries = sorted([(x, m, i) for i, (x, m) in enumerate(queries)], key=lambda q: q[1])
        
        ans = [0] * q
        t = Trie()
        idx = 0
        for x, m, qid in queries:
            while idx < n and nums[idx] <= m:
                t.insert(nums[idx])
                idx += 1
            if idx == 0:
                # 字典树为空
                ans[qid] = -1
            else:
                ans[qid] = t.getMaxXor(x)
        return ans
