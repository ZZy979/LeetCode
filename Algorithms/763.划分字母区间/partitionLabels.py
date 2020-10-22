class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        last = calc_last(S)
        ans = []
        left, right = 0, 0
        while right < len(S):
            i = left
            while i <= right:
                right = max(right, last[S[i]])
                i += 1
            ans.append(right - left + 1)
            left = right = right + 1
        return ans


def calc_last(s):
    last = {}
    for i, c in enumerate(s):
        last[c] = i
    return last
