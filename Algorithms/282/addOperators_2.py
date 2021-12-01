# 官方题解：回溯，604 ms
class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        n = len(num)
        ans = []

        def backtrack(expr: List[str], i: int, res: int, mul: int):
            if i == n:
                if res == target:
                    ans.append(''.join(expr))
                return
            signIndex = len(expr)
            if i > 0:
                expr.append('')  # 占位，下面填充符号
            val = 0
            for j in range(i, n):  # 枚举截取的数字长度（取多少位）
                if j > i and num[i] == '0':  # 数字可以是单个 0 但不能有前导零
                    break
                val = val * 10 + int(num[j])
                expr.append(num[j])
                if i == 0:  # 表达式开头不能添加符号
                    backtrack(expr, j + 1, val, val)
                else:  # 枚举符号
                    expr[signIndex] = '+'; backtrack(expr, j + 1, res + val, val)
                    expr[signIndex] = '-'; backtrack(expr, j + 1, res - val, -val)
                    expr[signIndex] = '*'; backtrack(expr, j + 1, res - mul + mul * val, mul * val)
            del expr[signIndex:]

        backtrack([], 0, 0, 0)
        return ans
