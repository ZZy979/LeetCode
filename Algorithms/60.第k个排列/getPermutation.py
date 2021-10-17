class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        factorial = [1]
        for i in range(1, n):
            factorial.append(factorial[-1] * i)
        
        k -= 1
        ans = ''
        nums = list(str(i) for i in range(1, n + 1))
        for i in range(1, n + 1):
            j, k = divmod(k, factorial[n - i])
            ans += nums.pop(j)
        return ans
