# 官方题解2：字典树
# 时间复杂度O(nlog C)，空间复杂度O(nlog C)，C是数组元素的范围
# 1504 ms
class TrieNode:
    def __init__(self):
        self.left = None
        self.right = None

class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        root = TrieNode()
        x = 0
        for i in range(1, len(nums)):
            add(root, nums[i - 1])
            x = max(x, check(root, nums[i]))
        return x


def add(root, num):
    cur = root
    for k in range(30, -1, -1):
        if num & (1 << k) == 0:
            if not cur.left:
                cur.left = TrieNode()
            cur = cur.left
        else:
            if not cur.right:
                cur.right = TrieNode()
            cur = cur.right

def check(root, num):
    cur = root
    x = 0
    for k in range(30, -1, -1):
        x <<= 1
        if num & (1 << k) == 0:
            if cur.right:
                cur = cur.right
                x += 1
            else:
                cur = cur.left
        else:
            if cur.left:
                cur = cur.left
                x += 1
            else:
                cur = cur.right
    return x
