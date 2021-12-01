class Solution:
    def isNumber(self, s: str) -> bool:
        try:
            _ = float(s)
            return True
        except ValueError:
            return False
