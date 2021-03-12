class Solution:
    def calculate(self, s: str) -> int:
        self.s = s.replace(' ', '')
        self.i = 0
        return self.expr()
    
    def expr(self):
        val = self.term()
        while self.i < len(self.s) and self.s[self.i] in '+-':
            op = self.s[self.i]
            self.i += 1
            num = self.term()
            val = val + num if op == '+' else val - num
        return val
    
    def term(self):
        val = self.factor()
        while self.i < len(self.s) and self.s[self.i] in '*/':
            op = self.s[self.i]
            self.i += 1
            num = self.factor()
            val = val * num if op == '*' else val // num
        return val
    
    def factor(self):
        num = 0
        while self.i < len(self.s) and self.s[self.i].isdigit():
            num = 10 * num + int(self.s[self.i])
            self.i += 1
        return num
