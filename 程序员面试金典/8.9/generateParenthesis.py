class Solution:
    def __init__(self):
        self.ans = []
    
    def generateParenthesis(self, n: int) -> List[str]:
        self.generate(n, 0, [])
        return self.ans
    
    def generate(self, n_left, n_unclosed, res):
        if n_left == 0:
            self.ans.append(''.join(res) + ')' * n_unclosed)
        else:
            res.append('(')
            self.generate(n_left - 1, n_unclosed + 1, res)
            res.pop()
            if n_unclosed > 0:
                res.append(')')
                self.generate(n_left, n_unclosed - 1, res)
                res.pop()
