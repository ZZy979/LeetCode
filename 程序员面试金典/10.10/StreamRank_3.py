# 方法3：二叉搜索树
# track时间复杂度：O(log n)，getRankOfNumber时间复杂度：O(log n)，空间复杂度：O(k)，k为不同数字的个数
# 84 ms
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.left_size = 1  # 左子树节点总数（包括自身）

def insert(node, v):
    if not node:
        return
    if v < node.val:
        node.left_size += 1
        if not node.left:
            node.left = TreeNode(v)
        else:
            insert(node.left, v)
    elif v > node.val:
        if not node.right:
            node.right = TreeNode(v)
        else:
            insert(node.right, v)
    else:
        node.left_size += 1

def find(node, v):
    if not node:
        return 0
    if v == node.val:
        return node.left_size
    elif v < node.val:
        return find(node.left, v)
    else:
        return node.left_size + find(node.right, v)


class StreamRank:

    def __init__(self):
        self.root = None

    def track(self, x: int) -> None:
        if not self.root:
            self.root = TreeNode(x)
        else:
            insert(self.root, x)

    def getRankOfNumber(self, x: int) -> int:
        return find(self.root, x)


# Your StreamRank object will be instantiated and called as such:
# obj = StreamRank()
# obj.track(x)
# param_2 = obj.getRankOfNumber(x)
