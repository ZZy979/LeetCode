from collections import Counter

class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        n = len(arr)
        count = Counter(arr)
        ans, deleted = 0, 0
        for _, c in count.most_common():
            deleted += c
            ans += 1
            if deleted >= n // 2:
                break
        return ans
