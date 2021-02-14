from collections import Counter

# 官方题解：将问题转化为“至多包含K个不同整数的子数组个数”
class Solution:
    def subarraysWithKDistinct(self, A: List[int], K: int) -> int:
        return at_most_k_distinct(A, K) - at_most_k_distinct(A, K - 1)

def at_most_k_distinct(a, k):
    c = Counter()
    left = ans = 0
    for right, x in enumerate(a):
        c[x] += 1
        while len(c) > k:
            y = a[left]
            c[y] -= 1
            if c[y] == 0:
                del c[y]
            left += 1
        ans += right - left + 1
    return ans
