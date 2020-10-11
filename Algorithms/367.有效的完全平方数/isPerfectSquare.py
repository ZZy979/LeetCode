class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        i = 0
        while i ** 2 <= num:
            if i ** 2 == num:
                return True
            else:
                i += 1
        return False
