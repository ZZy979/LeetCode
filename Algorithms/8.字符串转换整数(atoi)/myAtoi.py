import re

class Solution:
    def myAtoi(self, str: str) -> int:
        m = re.match(r'[+-]?\d+', str.strip())
        if m:
            x = int(m.group(0))
            return max(-2**31, min(2**31 - 1, x))
        else:
            return 0
