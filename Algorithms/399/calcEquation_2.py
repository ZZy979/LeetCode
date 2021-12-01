# 官方题解2：Floyd算法
# 时间复杂度O(ML+N³+QL)，空间复杂度O(NL+N²)，M为边数，Q为查询数，N为变量数
# 48 ms
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        nvars = 0
        variables = {}
        for e in equations:
            for v in e:
                if v not in variables:
                    variables[v] = nvars
                    nvars += 1
        
        graph = [[-1.0] * nvars for _ in range(nvars)]
        for (v1, v2), val in zip(equations, values):
            i1, i2 = variables[v1], variables[v2]
            graph[i1][i2] = val
            graph[i2][i1] = 1.0 / val
        
        for k in range(nvars):
            for i in range(nvars):
                for j in range(nvars):
                    if graph[i][k] > 0 and graph[k][j] > 0:
                        graph[i][j] = graph[i][k] * graph[k][j]
        
        ans = []
        for v1, v2 in queries:
            result = -1.0
            if v1 in variables and v2 in variables:
                i1, i2 = variables[v1], variables[v2]
                if graph[i1][i2] > 0:
                    result = graph[i1][i2]
            ans.append(result)
        return ans
