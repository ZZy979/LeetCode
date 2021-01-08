import math

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k %= n
        count = math.gcd(k, n)
        for start in range(count):
            cur, prev = start, nums[start]
            while True:
                next_ = (cur + k) % n
                nums[next_], prev = prev, nums[next_]
                cur = next_
                if cur == start:
                    break
