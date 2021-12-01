class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        left, right = max(weights), sum(weights)
        while left < right:
            mid = (left + right) // 2
            d = ship_days(weights, mid)
            if d <= D:
                right = mid
            else:
                left = mid + 1
        return left


def ship_days(weights, capacity):
    tmp, d = 0, 1
    for w in weights:
        tmp += w
        if tmp > capacity:
            d += 1
            tmp = w
    return d
