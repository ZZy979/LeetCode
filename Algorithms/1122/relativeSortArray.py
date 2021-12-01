class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        position = {x: i for i, x in enumerate(arr2)}
        arr1.sort(key=lambda x: position.get(x, 9999 + x))
        return arr1
