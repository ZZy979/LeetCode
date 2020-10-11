class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num < 2:
            return True
        left, right = 0, num
        while left < right:
            mid = (left + right) // 2
            s = mid ** 2
            if s == num:
                return True
            elif s > num:
                right = mid
            else:
                left = mid + 1
        return False
