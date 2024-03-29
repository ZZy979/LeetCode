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


# 官方题解中求解“至多包含K个不同整数的子数组个数”时为什么用区间长度表示增加的子数组个数？
# 即ans += right - left + 1为什么是合理的？

# 以A = [1, 2, 1, 2, 3], K = 2为例
# 至多包含2个不同整数的子数组：
# [1] [2] [1] [2] [3]
# [1, 2] [2, 1] [1, 2] [2, 3]
# [1, 2, 1] [2, 1, 2]
# [1, 2, 1, 2]

# 当left = 0, right = 0时
# [1] 2 1 2 3 答案增加一个子数组[1]

# 当left = 0, right = 1时
# [1 2] 1 2 3 答案增加[2]和[1, 2]两个子数组
# 由于前缀[1]已被计算过，因此只需计算以A[right] = 2结尾的子数组
# [2]和[1, 2]，恰好等于区间[left, right]的长度

# 当left = 0, right = 2时
# [1 2 1] 2 3 答案增加[1], [2, 1]和[1, 2, 1]三个子数组
# 由于前缀[1, 2]的子数组已被计算过，因此只需计算以A[right] = 1结尾的子数组
# [1], [2, 1]和[1, 2, 1]，恰好等于区间[left, right]的长度

# 当left = 0, right = 3时
# [1 2 1 2] 3 答案增加[2], [1, 2], [2, 1, 2]和[1, 2, 1, 2]四个子数组
# 由于前缀[1, 2, 1]的子数组已被计算过，因此只需计算以A[right] = 2结尾的子数组
# [2], [1, 2], [2, 1, 2]和[1, 2, 1, 2]，恰好等于区间[left, right]的长度

# 当left = 3, right = 4时
# 1 2 1 [2 3] 答案增加[3]和[2, 3]两个子数组
# 由于前缀[2]在right = 3时已被计算过，因此只需计算以A[right] = 3结尾的子数组
# [3]和[2, 3]，恰好等于区间[left, right]的长度
