# 官方题解2：秦九韶算法（正序遍历）
class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        q = 1337
        ans = 1
        for e in b:
            ans = pow(ans, 10, q) * pow(a, e, q) % q
        return ans
