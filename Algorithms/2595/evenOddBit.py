class Solution:
    def evenOddBit(self, n: int) -> List[int]:
        return [(n & 0x55555555).bit_count(), (n & 0xAAAAAAAA).bit_count()]
