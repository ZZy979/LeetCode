class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        rank = {s: i + 1 for i, s in enumerate(sorted(score, reverse=True))}
        return [
            'Gold Medal' if rank[s] == 1 \
            else 'Silver Medal' if rank[s] == 2 \
            else 'Bronze Medal' if rank[s] == 3 \
            else str(rank[s])
            for s in score
        ]
