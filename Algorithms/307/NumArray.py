# 官方题解1：分块处理
# 时间复杂度：构造函数为O(n)，update函数为O(1)，sumRange函数为O(sqrt(n))
# 空间复杂度：O(sqrt(n))
class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.block_size = int(math.sqrt(len(nums)))
        self.sums = [sum(nums[i:i + self.block_size]) for i in range(0, len(nums), self.block_size)]

    def update(self, index: int, val: int) -> None:
        self.sums[index // self.block_size] += val - self.nums[index]
        self.nums[index] = val

    def sumRange(self, left: int, right: int) -> int:
        b1 = left // self.block_size
        b2 = right // self.block_size
        if b1 == b2:
            return sum(self.nums[left:right + 1])
        else:
            return sum(self.nums[left:(b1 + 1) * self.block_size]) + sum(self.sums[b1 + 1:b2]) + sum(self.nums[b2 * self.block_size:right + 1])


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)
