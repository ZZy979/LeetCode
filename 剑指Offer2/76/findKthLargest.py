import random

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return quick_select(nums, 0, len(nums) - 1, len(nums) - k)


def quick_select(a, l, r, index):
    p = partition(a, l, r)
    if p == index:
        return a[p]
    elif p < index:
        return quick_select(a, p + 1, r, index)
    else:
        return quick_select(a, l, p - 1, index)


def partition(a, l, r):
    i = random.randint(l, r)
    a[i], a[r] = a[r], a[i]
    pivot = a[r]
    p = l
    for i in range(l, r):
        if a[i] < pivot:
            a[p], a[i] = a[i], a[p]
            p += 1
    a[p], a[r] = a[r], a[p]
    return p
