import time

class Solution:
    def dayOfYear(self, date: str) -> int:
        return time.strptime(date, '%Y-%m-%d').tm_yday
