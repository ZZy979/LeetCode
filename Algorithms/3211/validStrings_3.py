# 递归
class Solution:
    def validStrings(self, n: int) -> List[str]:
        return list(generate(n, ''))

def generate(n, temp):
    if len(temp) == n:
        yield temp
    elif not temp or temp[-1] == '1':
        yield from generate(n, temp + '0')
        yield from generate(n, temp + '1')
    else:
        yield from generate(n, temp + '1')
