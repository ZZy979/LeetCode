# 官方题解：模拟
# allocate时间复杂度O(n)，freeMemory时间复杂度O(n)，空间复杂度O(n)
class Allocator:

    def __init__(self, n: int):
        self.n = n
        self.memory = [0] * n

    def allocate(self, size: int, mID: int) -> int:
        count = 0
        for i, m in enumerate(self.memory):
            if m == 0:
                count += 1
                if count >= size:
                    start = i - size + 1
                    self.memory[start:start + size] = [mID] * size
                    return start
            else:
                count = 0
        return -1

    def freeMemory(self, mID: int) -> int:
        freed = 0
        for i, m in enumerate(self.memory):
            if m == mID:
                freed += 1
                self.memory[i] = 0
        return freed


# Your Allocator object will be instantiated and called as such:
# obj = Allocator(n)
# param_1 = obj.allocate(size,mID)
# param_2 = obj.freeMemory(mID)
