class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        arr = [first]
        for x in encoded:
            arr.append(arr[-1] ^ x)
        return arr
