from collections import Counter

# 评论区解法
class Solution:
    def subarraysWithKDistinct(self, A: List[int], K: int) -> int:
        counter = Counter()
        res = left = left_forward = 0
        for right in range(len(A)):
            counter[A[right]] += 1
            if len(counter) == K:
                if left > 0 and A[left - 1] != A[right]:
                    left_forward = 0
                while len(counter) == K:
                    counter[A[left]] -= 1
                    if counter[A[left]] == 0:
                        del counter[A[left]]
                    left += 1
                    left_forward += 1
            res += left_forward
        return res
