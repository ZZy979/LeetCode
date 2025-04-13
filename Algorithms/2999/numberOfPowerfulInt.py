class Solution:
    def numberOfPowerfulInt(self, start: int, finish: int, limit: int, s: str) -> int:
        return num_powerful_int(finish, limit, s) - num_powerful_int(start - 1, limit, s)

def num_powerful_int(end, limit, suffix):
    """计算[0, end]内的强大整数数目"""
    # 例如limit=6，则end的前缀部分为4729等价于4666，整数数目为4*7³+6*7²+6*7+7+1，刚好是7进制数5000的值
    if end < 0:
        return 0
    q, r = divmod(end, 10**len(suffix))
    s = str(q)
    n = len(s)
    i = 0
    while i < n and int(s[i]) <= limit:
        i += 1
    return (int(s[:i] or '0', limit + 1) + 1) * pow(limit + 1, n - i) - (i == n and r < int(suffix))
