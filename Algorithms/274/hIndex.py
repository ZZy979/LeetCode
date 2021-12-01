class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        citations.sort()
        for i in range(n):
            if (h := n - i) <= citations[i]:
                return h
        return 0
