class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        m = defaultdict(int)
        n, l, ans = len(answerKey), 0, 0
        for r in range(n):
            m[answerKey[r]] += 1
            if min(m["T"], m["F"]) > k:
                m[answerKey[l]] -= 1
                l += 1
            ans = max(ans, r - l + 1)
        return ans
