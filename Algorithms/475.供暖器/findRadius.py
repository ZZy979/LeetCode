class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()
        i = 0
        min_radius = 0
        for j in range(len(heaters) - 1):
            while i < len(houses) and houses[i] <= (heaters[j] + heaters[j + 1]) // 2:
                min_radius = max(min_radius, abs(houses[i] - heaters[j]))
                i += 1
        while i < len(houses):
            min_radius = max(min_radius, abs(houses[i] - heaters[-1]))
            i += 1
        return min_radius
