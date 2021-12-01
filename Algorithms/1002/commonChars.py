from collections import Counter
import itertools

class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        c = Counter(A[0])
        for i in range(1, len(A)):
            temp_c = Counter(A[i])
            for k in itertools.chain(c, temp_c):
                c[k] = min(c[k], temp_c[k])
        ans = []
        for k in c:
            for i in range(c[k]):
                ans.append(k)
        return ans
