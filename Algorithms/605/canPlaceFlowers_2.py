# 评论区解法：任意位置处只要连续出现3个0就可以栽上一棵花
# 时间复杂度O(n)
# 68 ms
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        flowerbed = [0] + flowerbed + [0]
        for i in range(1, len(flowerbed) - 1):
            if flowerbed[i - 1] == flowerbed[i] == flowerbed[i + 1] == 0:
                flowerbed[i] = 1
                n -= 1
        return n <= 0
