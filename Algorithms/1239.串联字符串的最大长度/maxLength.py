class Solution:
    def maxLength(self, arr: List[str]) -> int:
        appeared = [False] * 26
        return backtrack(arr, 0, appeared)


def backtrack(arr, i, appeared):
    if i >= len(arr):
        return sum(appeared)
    new_appeared = appeared.copy()
    ans = 0
    for c in arr[i]:
        if new_appeared[ord(c) - ord('a')]:
            break
        new_appeared[ord(c) - ord('a')] = True
    else:
        ans = backtrack(arr, i + 1, new_appeared)
    return max(ans, backtrack(arr, i + 1, appeared))
