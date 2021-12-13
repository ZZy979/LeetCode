import bisect
from collections import Counter

class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        self.times = times
        self.top = []
        votes = Counter()
        max_votes = 0
        for p in persons:
            votes[p] += 1
            if votes[p] >= max_votes:
                max_votes = votes[p]
                self.top.append(p)
            else:
                self.top.append(self.top[-1])

    def q(self, t: int) -> int:
        return self.top[bisect.bisect_right(self.times, t) - 1]


# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)
