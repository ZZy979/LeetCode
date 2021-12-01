class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        last = {c: i for i, c in enumerate(S)}
        ans = []
        left = right = 0
        for i in range(len(S)):
            right = max(right, last[S[i]])
            if i == right:
                ans.append(right - left + 1)
                left = right = i + 1
        return ans
