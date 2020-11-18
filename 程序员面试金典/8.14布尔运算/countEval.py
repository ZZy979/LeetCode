class Solution:

    def __init__(self):
        self.memo = {}

    def countEval(self, s: str, result: int) -> int:
        if not s:
            return 0
        elif len(s) == 1:
            return int(int(s) == result)
        elif (result, s) in self.memo:
            return self.memo[(result, s)]
        
        ways = 0
        for i in range(1, len(s), 2):
            op = s[i]
            left, right = s[:i], s[i + 1:]
            left_true, left_false = self.countEval(left, 1), self.countEval(left, 0)
            right_true, right_false = self.countEval(right, 1), self.countEval(right, 0)
            total = (left_true + left_false) * (right_true + right_false)
            total_true = left_true * right_true if op == '&' else \
                left_true * right_true + left_false * right_true + left_true * right_false if op == '|' else \
                left_true * right_false + left_false * right_true
            ways += total_true if result == 1 else total - total_true
        self.memo[(result, s)] = ways
        return ways
