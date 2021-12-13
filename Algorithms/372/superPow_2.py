# 官方题解1：倒序遍历
class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        q = 1337
        ans = 1
        for e in reversed(b):
            ans = ans * pow(a, e, q) % q
            a = pow(a, 10, q)
        return ans
