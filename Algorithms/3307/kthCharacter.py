class Solution:
    def kthCharacter(self, k: int, operations: List[int]) -> str:
        n = sum(op for bit, op in zip(bin(k - 1)[:1:-1], operations) if bit == '1')
        return chr(ord('a') + n % 26)
