import random

# 快排思想
class Solution:
    def smallestK(self, arr: List[int], k: int) -> List[int]:
        if k == 0:
            return []
        quick_select(arr, 0, len(arr) - 1, k)
        return arr[:k]


def quick_select(a, l, r, k):
    q = random_partition(a, l, r)
    n = q - l + 1
    if n > k:
        quick_select(a, l, q - 1, k)
    elif n < k:
        quick_select(a, q + 1, r, k - n)

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
