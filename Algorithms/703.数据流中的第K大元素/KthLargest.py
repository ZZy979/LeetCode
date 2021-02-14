import bisect

# 二分查找插入，时间复杂度O(n)
# 128 ms
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = sorted(-x for x in nums)

    def add(self, val: int) -> int:
        i = bisect.bisect(self.nums, -val)
        self.nums.insert(i, -val)
        return -self.nums[self.k - 1]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
