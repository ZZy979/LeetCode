from collections import defaultdict

# 个人方法：寻找每个人的正确位置
# 800 ms
class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        n_front = defaultdict(list)
        for h, k in people:
            n_front[h].append(k)

        res = [None] * len(people)
        for h in sorted(n_front.keys()):
            for k in n_front[h]:
                i, c = 0, 0
                while i < len(res) and c < k:
                    if not res[i] or res[i][0] == h:
                        c += 1
                    i += 1
                while res[i]:
                    i += 1
                res[i] = [h, k]
        return res
