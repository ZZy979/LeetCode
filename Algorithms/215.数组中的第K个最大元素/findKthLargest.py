import random

# 官方题解1：基于快速排序的选择方法
# 时间复杂度O(n)，空间复杂度O(log n)
# 48 ms
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return quick_select(nums, 0, len(nums) - 1, len(nums) - k)

def quick_select(a, l, r, index):
    q = random_partition(a, l, r)
    if q == index:
        return a[q]
    else:
        return quick_select(a, q + 1, r, index) if q < index else quick_select(a, l, q - 1, index)

def random_partition(a, l, r):
    i = random.randint(l, r)
    a[i], a[r] = a[r], a[i]
    return partition(a, l, r)

def partition(a, l, r):
    x = a[r]
    i = l - 1
    for j in range(l, r):
        if a[j] <= x:
            i += 1
            a[i], a[j] = a[j], a[i]
    i += 1
    a[i], a[r] = a[r], a[i]
    return i
