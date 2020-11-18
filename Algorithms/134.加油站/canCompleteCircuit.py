# 暴力法
# 4416 ms
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        for p in range(len(gas)):
            if gas[p] >= cost[p]:
                if can_complete_from(gas, cost, p):
                    return p
        return -1


def can_complete_from(gas, cost, start):
    p = start
    fuel = gas[start]
    for i in range(len(gas) - 1):
        if fuel < cost[p]:
            return False
        fuel -= cost[p]
        p = (p + 1) % len(gas)
        fuel += gas[p]
    return fuel >= cost[p]
