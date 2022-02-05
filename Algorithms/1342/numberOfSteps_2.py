class Solution:
    def numberOfSteps(self, num: int) -> int:
        return 0 if num == 0 else num.bit_length() - 1 + bit_count(num)


def bit_count(num):
    count = 0
    while num > 0:
        count += (num & 1)
        num >>= 1
    return count
