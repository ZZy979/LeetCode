class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        w = n - k
        m = s = sum(cardPoints[:w])
        for i in range(w, n):
            s += cardPoints[i] - cardPoints[i - w]
            m = min(m, s)
        return sum(cardPoints) - m
