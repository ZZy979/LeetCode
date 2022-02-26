# 评论区解法：字符串替换
class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        last = ''
        while dominoes != last:
            last = dominoes
            dominoes = dominoes.replace('R.L', 'T').replace('.L', 'LL').replace('R.', 'RR').replace('T', 'R.L')
        return dominoes
