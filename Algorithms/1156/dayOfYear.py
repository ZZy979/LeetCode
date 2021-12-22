from datetime import datetime

class Solution:
    def dayOfYear(self, date: str) -> int:
        d = datetime.strptime(date, '%Y-%m-%d')
        return (d - datetime(d.year, 1, 1)).days + 1
