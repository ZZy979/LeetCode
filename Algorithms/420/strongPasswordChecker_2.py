# 评论区解法
class Solution:
    def strongPasswordChecker(self, password: str) -> int:
        n = len(password)
        lack = 3 - sum(bool(re.search(reg, password)) for reg in ['[a-z]', '[A-Z]', '[0-9]'])
        if n < 6:
            return max(6-n, lack)
        pq, i = [], 0
        for j in range(n):
            if j==n-1 or password[j+1] != password[j]:
                a = j-i+1
                if a>=3:
                    heappush(pq, (a%3, a))
                i = j+1
        res = 0
        while pq and n>20:
            _, a = heappop(pq)
            if a>3:
                heappush(pq, ((a-1)%3, a-1))
            n -= 1
            res += 1
        return res + max(0, n-20) + max(sum(a//3 for _, a in pq), lack)
