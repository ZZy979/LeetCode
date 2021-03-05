class Solution:
    def countBits(self, num: int) -> List[int]:
        if num == 0:
            return [0]
        ans = [0] * (num + 1)
        ans[1] = 1
        left = 2
        while 2 * left - 1 <= num:
            for i in range(left, 2 * left):
                ans[i] = ans[i - left] + 1
            left *= 2
        for i in range(left, num + 1):
            ans[i] = ans[i - left] + 1
        return ans
