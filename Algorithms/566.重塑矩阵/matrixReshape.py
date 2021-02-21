class Solution:
    def matrixReshape(self, nums: List[List[int]], r: int, c: int) -> List[List[int]]:
        r0, c0 = len(nums), len(nums[0])
        if r0 * c0 != r * c:
            return nums
        res = [[0] * c for _ in range(r)]
        for idx in range(r0 * c0):
            i, j = divmod(idx, c)
            i0, j0 = divmod(idx, c0)
            res[i][j] = nums[i0][j0]
        return res
