from itertools import combinations, compress

class Solution:
    def readBinaryWatch(self, num: int) -> List[str]:
        return list('{:d}:{:02d}'.format(h, m) for h in range(12) for m in range(60) if bin(h).count('1') + bin(m).count('1') == num)
