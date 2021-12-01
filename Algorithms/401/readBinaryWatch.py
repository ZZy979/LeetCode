from itertools import combinations, compress

class Solution:
    def readBinaryWatch(self, num: int) -> List[str]:
        hours = [8, 4, 2, 1]
        minutes = [32, 16, 8, 4, 2, 1]
        return [
            "{:d}:{:02d}".format(sum(compress(hours, led[:4])), sum(compress(minutes, led[4:])))
            for led in (
                tuple(int(p in t) for p in range(10))
                for t in combinations(range(10), num)
            )
            if sum(compress(hours, led[:4])) < 12 and sum(compress(minutes, led[4:])) < 60
        ]
