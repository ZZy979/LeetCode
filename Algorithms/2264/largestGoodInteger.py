class Solution:
    def largestGoodInteger(self, num: str) -> str:
        return max((num[i] for i in range(len(num) - 2) if num[i] == num[i + 1] == num[i + 2]), default='') * 3
