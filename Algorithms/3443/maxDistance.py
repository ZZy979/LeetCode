class Solution:
    def maxDistance(self, s: str, k: int) -> int:
        ans = 0
        north = south = east = west = 0
        for c in s:
            if c == 'N':
                north += 1
            elif c == 'S':
                south += 1
            elif c == 'E':
                east += 1
            elif c == 'W':
                west += 1
            ans = max(ans, abs(north - south) + abs(east - west) + 2 * min(k, min(north, south) + min(east, west)))
        return ans
