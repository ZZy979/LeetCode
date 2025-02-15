import itertools

class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        ans = list(itertools.accumulate(reversed(arr[1:]), max, initial=-1))
        ans.reverse()
        return ans
