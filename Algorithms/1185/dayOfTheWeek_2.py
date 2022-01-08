class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        days = (year - 1971) * 365 + (year - 1969) // 4  # 1971~2099没有整除100的
        days += sum(month_days[:month - 1]) + (month >= 3 and (year % 4 == 0 and year % 100 != 0 or year % 400 == 0))
        days += day
        return weekdays[(days + 3) % 7]
