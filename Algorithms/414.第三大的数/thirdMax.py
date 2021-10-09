class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        a = b = c = -0xffffffff
        for num in nums:
            if num > a:
                a, b, c = num, a, b
            elif b < num < a:
                b, c = num, b
            elif c < num < b:
                c = num
        return a if c == -0xffffffff else c
