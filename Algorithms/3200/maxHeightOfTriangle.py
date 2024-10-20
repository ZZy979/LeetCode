from math import sqrt, floor

class Solution:
    def maxHeightOfTriangle(self, red: int, blue: int) -> int:
        if red < blue:
            red, blue = blue, red
        # 第1行是蓝球，共2k行，k^2 <= blue且k^2+k <= red
        k1 = min(floor(sqrt(blue)), floor(sqrt(red + 0.25) - 0.5))
        # 第1行是红球，共2k-1行，k^2 <= red且k^2-k <= blue
        k2 = min(floor(sqrt(red)), floor(sqrt(blue + 0.25) + 0.5))
        return max(2 * k1, 2 * k2 - 1)
