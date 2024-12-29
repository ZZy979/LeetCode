class Solution:
    def rankTeams(self, votes: List[str]) -> str:
        ranking = {t: [0] * len(votes[0]) for t in votes[0]}
        for v in votes:
            for i, t in enumerate(v):
                ranking[t][i] += 1
        return ''.join(sorted(votes[0], key=lambda t: (ranking[t], -ord(t)), reverse=True))
