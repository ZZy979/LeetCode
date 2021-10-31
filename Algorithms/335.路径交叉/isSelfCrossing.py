class Solution:
    def isSelfCrossing(self, distance: List[int]) -> bool:
        return any(
            (distance[i] >= distance[i - 2] and distance[i - 1] <= distance[i - 3]) \
            or (i == 4 and distance[3] == distance[1] and distance[4] >= distance[2] - distance[0]) \
            or (i >= 5 and distance[i - 3] - distance[i - 5] <= distance[i - 1] <= distance[i - 3] and distance[i] >= distance[i - 2] - distance[i - 4] and distance[i - 2] > distance[i - 4])
            for i in range(3, len(distance))
        )
