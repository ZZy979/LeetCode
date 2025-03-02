from sortedcontainers import SortedDict

# 有序映射
# allocate时间复杂度O(b)，freeMemory时间复杂度O(blog b)，其中b为已分配块的数量
# 空间复杂度O(b)
class Allocator:

    def __init__(self, n: int):
        self.n = n
        self.blocks = SortedDict()

    def find_free(self, size):
        start = 0
        for idx, block in self.blocks.items():
            if idx - start >= size:
                return start
            start = idx + block[0]
        if self.n - start >= size:
            return start
        return -1

    def allocate(self, size: int, mID: int) -> int:
        idx = self.find_free(size)
        if idx != -1:
            self.blocks[idx] = (size, mID)
        return idx

    def freeMemory(self, mID: int) -> int:
        indices = []
        freed = 0
        for idx, block in self.blocks.items():
            if block[1] == mID:
                indices.append(idx)
                freed += block[0]
        for idx in indices:
            del self.blocks[idx]
        return freed


# Your Allocator object will be instantiated and called as such:
# obj = Allocator(n)
# param_1 = obj.allocate(size,mID)
# param_2 = obj.freeMemory(mID)
