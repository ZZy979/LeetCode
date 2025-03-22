class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        index = mx = -1
        for i, row in enumerate(mat):
            if (n := row.count(1)) > mx:
                index, mx = i, n
        return [index, mx]
