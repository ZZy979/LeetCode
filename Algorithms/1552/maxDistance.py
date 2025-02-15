# 二分查找，时间复杂度O(nlog n + nlog C)，空间复杂度O(log n)（排序需要的栈空间）
class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        left, right, ans = 1, position[-1], 0
        while left <= right:
            d = (left + right) // 2
            if check(position, m, d):
                ans = d
                left = d + 1
            else:
                right = d - 1
        return ans

def check(position, m, dist):
    """是否能够将m个球放到篮子里，使得任意两球间的最小距离为dist"""
    last = float('-inf')
    for p in position:
        if p - last >= dist:
            m -= 1
            last = p
        if m == 0:
            return True
    return False
