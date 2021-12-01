from collections import deque

# 官方题解1：广度优先搜索
# 时间复杂度O(ML+Q(L+M))，空间复杂度O(NL+M)，M为边数，Q为查询数，N为变量数
# 36 ms
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        nvars = 0
        variables = {}
        for e in equations:
            for v in e:
                if v not in variables:
                    variables[v] = nvars
                    nvars += 1
        
        edges = [[] for _ in range(nvars)]
        for (v1, v2), val in zip(equations, values):
            i1, i2 = variables[v1], variables[v2]
            edges[i1].append((i2, val))
            edges[i2].append((i1, 1.0 / val))
        
        ans = []
        for v1, v2 in queries:
            result = -1.0
            if v1 in variables and v2 in variables:
                start, end = variables[v1], variables[v2]
                ratios = [-1.0] * nvars
                ratios[start] = 1.0
                if start == end:
                    result = 1.0
                else:
                    queue = deque([start])
                    while queue:
                        x = queue.popleft()
                        for y, ratio in edges[x]:
                            if ratios[y] < 0:
                                ratios[y] = ratios[x] * ratio
                                queue.append(y)
                    result = ratios[end]
            ans.append(result)
        return ans
