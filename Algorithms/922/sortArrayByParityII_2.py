# 228 ms
class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        even, odd = [], []
        for i in A:
            if i % 2:
                odd.append(i)
            else:
                even.append(i)
        ans = []
        for i, j in zip(even, odd):
            ans.append(i)
            ans.append(j)
        return ans
