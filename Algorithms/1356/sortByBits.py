class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        a = [(bit_count(x), x) for x in arr]
        a.sort()
        return [x for c, x in a]


def bit_count(x):
    count = 0
    while x:
        count += x & 1
        x >>= 1
    return count
