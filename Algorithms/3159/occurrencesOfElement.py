class Solution:
    def occurrencesOfElement(self, nums: List[int], queries: List[int], x: int) -> List[int]:
        index = [i for i in range(len(nums)) if nums[i] == x]
        return [index[q - 1] if q <= len(index) else -1 for q in queries]
