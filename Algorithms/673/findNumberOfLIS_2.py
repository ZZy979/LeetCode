# 官方题解2：贪心+二分查找+前缀和
class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        d, cnt = [], []
        for v in nums:
            i = bisect(len(d), lambda i: d[i][-1] >= v)
            c = 1
            if i > 0:
                k = bisect(len(d[i - 1]), lambda k: d[i - 1][k] < v)
                c = cnt[i - 1][-1] - cnt[i - 1][k]
            if i == len(d):
                d.append([v])
                cnt.append([0, c])
            else:
                d[i].append(v)
                cnt[i].append(cnt[i][-1] + c)
        return cnt[-1][-1]

def bisect(n: int, f: Callable[[int], bool]) -> int:
    l, r = 0, n
    while l < r:
        mid = (l + r) // 2
        if f(mid):
            r = mid
        else:
            l = mid + 1
    return l
