# 方法1：减法
class Solution:
    def swapNumbers(self, numbers: List[int]) -> List[int]:
        numbers[0] -= numbers[1]
        numbers[1] += numbers[0]
        numbers[0] = numbers[1] - numbers[0]
        return numbers
