class Solution:
    def minMaxDifference(self, num: int) -> int:
        return replace(num, '9') - replace(num, '0')

def replace(num, r):
    digits = list(str(num))
    for d in digits:
        if d != r:
            return int(''.join(r if n == d else n for n in digits))
    return num
