class Solution:
    def findContinuousSequence(self, target: int) -> List[List[int]]:
        ans = []
        for m in range(2, target // 2 + 1):
            if target % m == 0 and target // m % 2 == 1:
                k = (target // m - 1) // 2
                if m > k:
                    ans.append(list(range(m - k, m + k + 1)))
            if target % (2 * m + 1) == 0:
                k = target // (2 * m + 1)
                if m > k - 1:
                    ans.append(list(range(m - k + 1, m + k + 1)))
        return ans
