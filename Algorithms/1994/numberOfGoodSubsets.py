class Solution:
    def numberOfGoodSubsets(self, nums: List[int]) -> int:
        ct, mod = Counter(nums), 10**9+7
        d = Counter()
        d[1] = (1 << ct[1]) % mod
        for num in [2, 3, 5, 6, 7, 10, 11, 13, 14, 15, 17, 19, 21, 22, 23, 26, 29, 30]:
            for x in list(d):
                if math.gcd(num, x) == 1:
                    d[num*x] += ct[num] * d[x]
                    d[num*x] %= mod
        return (sum(d.values()) - d[1]) % mod
