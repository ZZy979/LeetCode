# 官方题解2：从高到低考虑
# 92 ms
class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort(key=lambda p : (-p[0], p[1]))
        res = []
        for p in people:
            res.insert(p[1], p)
        return res
