# 暴力法
class Solution:
    def validStrings(self, n: int) -> List[str]:
        return [f'{x:0{n}b}' for x in range(2**n) if '00' not in f'{x:0{n}b}']
