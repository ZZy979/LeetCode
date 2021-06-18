import re

class Solution:
    def isNumber(self, s: str) -> bool:
        return bool(re.fullmatch(r'[+-]?((\d+\.?)|(\d*\.\d+))([eE][+-]?\d+)?', s))
