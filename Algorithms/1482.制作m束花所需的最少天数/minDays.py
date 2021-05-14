class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        n = len(bloomDay)
        if n < m * k:
            return -1
        left, right = 1, max(bloomDay)
        while left < right:
            mid = (left + right) // 2
            if can_make(bloomDay, mid, m, k):
                right = mid
            else:
                left = mid + 1
        return left


def can_make(bloomDay, x, m, k):
    bouquets = flowers = 0
    for b in bloomDay:
        if b <= x:
            flowers += 1
            if flowers == k:
                bouquets += 1
                flowers = 0
        else:
            flowers = 0
    return bouquets >= m
