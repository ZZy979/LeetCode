# 贪心，时间复杂度O(m)
# 52 ms
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        length = len(flowerbed)
        count, i = 0, 0
        while i < length:
            while i < length and (flowerbed[i] == 1 or i > 0 and flowerbed[i - 1] == 1 or i < length - 1 and flowerbed[i + 1] == 1):
                i += 1
            if i < length:
                flowerbed[i] = 1
                count += 1
                i += 1
        return count >= n
